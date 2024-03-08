import tokenize
import os
import shutil
import sys

class Reindenter:

    def __init__(self, lines):
        self.find_stmt = 1  # next token begins a fresh stmt?
        self.level = 0      # current indent level

        # Raw file lines.
        self.raw = lines
        self.lines = [_rstrip(line).expandtabs() + "\n"
                        for line in self.raw]
        self.lines.insert(0, None)
        self.index = 1
        self.stats = []
        self.newlines = '\n'

    def run(self):
        tokens = tokenize.generate_tokens(self.getline)
        for _token in tokens:
            self.tokeneater(*_token)
        # Remove trailing empty lines.
        lines = self.lines
        while lines and lines[-1] == "\n":
            lines.pop()
        # Sentinel.
        stats = self.stats
        stats.append((len(lines), 0))
        # Map count of leading spaces to # we want.
        have2want = {}
        # Program after transformation.
        after = self.after = []
        # Copy over initial empty lines -- there's nothing to do until
        # we see a line with *something* on it.
        i = stats[0][0]
        after.extend(lines[1:i])
        for i in range(len(stats) - 1):
            thisstmt, thislevel = stats[i]
            nextstmt = stats[i + 1][0]
            have = getlspace(lines[thisstmt])
            want = thislevel * 4
            if want < 0:
                # A comment line.
                if have:
                    # An indented comment line.  If we saw the same
                    # indentation before, reuse what it most recently
                    # mapped to.
                    want = have2want.get(have, -1)
                    if want < 0:
                        # Then it probably belongs to the next real stmt.
                        for j in range(i + 1, len(stats) - 1):
                            jline, jlevel = stats[j]
                            if jlevel >= 0:
                                if have == getlspace(lines[jline]):
                                    want = jlevel * 4
                                break
                    if want < 0:           # Maybe it's a hanging
                                        # comment like this one,
                        # in which case we should shift it like its base
                        # line got shifted.
                        for j in range(i - 1, -1, -1):
                            jline, jlevel = stats[j]
                            if jlevel >= 0:
                                want = have + (getlspace(after[jline - 1]) -
                                            getlspace(lines[jline]))
                                break
                    if want < 0:
                        # Still no luck -- leave it alone.
                        want = have
                else:
                    want = 0
            assert want >= 0
            have2want[have] = want
            diff = want - have
            if diff == 0 or have == 0:
                after.extend(lines[thisstmt:nextstmt])
            else:
                for line in lines[thisstmt:nextstmt]:
                    if diff > 0:
                        if line == "\n":
                            after.append(line)
                        else:
                            after.append(" " * diff + line)
                    else:
                        remove = min(getlspace(line), -diff)
                        after.append(line[remove:])
        return self.raw != self.after

    def write(self, f):
        f.writelines(self.after)

    # Line-getter for tokenize.
    def getline(self):
        if self.index >= len(self.lines):
            line = ""
        else:
            line = self.lines[self.index]
            self.index += 1
        return line

    # Line-eater for tokenize.
    def tokeneater(self, type, token, slinecol, end, line,
                INDENT=tokenize.INDENT,
                DEDENT=tokenize.DEDENT,
                NEWLINE=tokenize.NEWLINE,
                COMMENT=tokenize.COMMENT,
                NL=tokenize.NL):

        if type == NEWLINE:
            # A program statement, or ENDMARKER, will eventually follow,
            # after some (possibly empty) run of tokens of the form
            #     (NL | COMMENT)* (INDENT | DEDENT+)?
            self.find_stmt = 1

        elif type == INDENT:
            self.find_stmt = 1
            self.level += 1

        elif type == DEDENT:
            self.find_stmt = 1
            self.level -= 1

        elif type == COMMENT:
            if self.find_stmt:
                self.stats.append((slinecol[0], -1))
                # but we're still looking for a new stmt, so leave
                # find_stmt alone

        elif type == NL:
            pass

        elif self.find_stmt:
            # This is the first "real token" following a NEWLINE, so it
            # must be the first token of the next program statement, or an
            # ENDMARKER.
            self.find_stmt = 0
            if line:   # not endmarker
                self.stats.append((slinecol[0], self.level))


# Count number of leading blanks.
def getlspace(line):
    i, n = 0, len(line)
    while i < n and line[i] == " ":
        i += 1
    return i

def _rstrip(line, JUNK='\n \t'):
    """Return line stripped of trailing spaces, tabs, newlines."""
    i = len(line)
    while i > 0 and line[i - 1] in JUNK:
        i -= 1
    return line[:i]

def reindent_lines(lines_list):
    """Reindent a list of Python lines."""

    try:
        r = Reindenter(lines_list)
        r.run()
        return [line.rstrip() for line in r.after if line]
    except Exception as e:
        return lines_list

if __name__ == '__main__':
    # Test the function
    lines_to_reindent = [
        "def func():",
        "\tif True:",
        "\t\tprint('Hello')",
        "\telse:",
        "\tprint('World')",
        "print('Outside')"
    ]

    reindented_lines = reindent_lines(lines_to_reindent)
    for line in reindented_lines:
        print(line)