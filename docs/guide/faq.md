Our vision empowers users to achieve 10x more with AI. The LLM Automatic Computer Framework (L2MAC) transforms cutting-edge LLMs into user-directed, reusable, and efficient AI assistants capable of autonomously executing complex real-world tasks, revolutionizing productivity and code generation.

### Convenient Link for Sharing this Document:

```
- FAQ https://github.com/samholt/L2MAC/blob/master/docs/faq.md
```

### Link

1.  Code：https://github.com/samholt/L2MAC/
2.  Roadmap：https://github.com/samholt/L2MAC/blob/master/docs/roadmap.md

### How do I become a contributor?

1.  Choose a task from the Roadmap (or you can propose one). By submitting a PR, you can become a contributor and join the dev team.
2.  Current contributors come from backgrounds including Oxford/Cambridge Universities and companies.

### Become the Chief Evangelist at for the L2MAC Community

Join us as the Chief Evangelist, a dynamic role that changes hands every month, fueling continuous innovation and fresh ideas within our community. Here's what you'll do:

- **Community Leadership and Support:** Take charge of maintaining essential community resources such as FAQ documents, announcements, and GitHub READMEs. Ensure that every community member has the information they need to thrive.
- **Rapid Response:** Act as the first point of contact for community inquiries. Your goal will be to respond to questions on platforms like GitHub Issues and Discord within 30 minutes, ensuring our community remains informed and engaged.
- **Foster Positive Engagement:** Cultivate an environment that is not only enthusiastic and genuine but also welcoming. We aim to make every member feel valued and supported.
- **Encourage Active Participation:** Inspire community members to contribute to projects that push the boundaries towards achieving tools to 10x people's work productivity. Your encouragement will help harness the collective expertise and passion of our community.
- **Event Coordination (Optional):** Have a flair for event planning? You can choose to organize small-scale events, such as hackathons, which are crucial for sparking innovation and collaboration within the community.

**Why Join Us?**

This role offers the unique opportunity to be at the forefront of the AI revolution, engage with like-minded individuals, and play a pivotal part in steering our community towards significant contributions in the field of AGI. If you are passionate about AI, eager to help others, and ready to lead, the Chief Evangelist position is your platform to shine and make an impact. Interested applicants for the position, please email `sih31 (at) cam.ac.uk`.


### FAQ

1.  Code tests are failing due to an import error:
    1. At present any package the LLM agent tries to use must already be installed on your current virtualenv that you are running L2MAC from. Therefore, it is best to find out which packages L2MAC is trying to use and install them, and or the specific package version of them. We plan to fix this in the future with self-created virtualenvs per codebase generation; see the [roadmap](./roadmap), and welcome contributions on this.
2.  Want to join the contributor team? How to proceed?
    1.  Merging a PR will get you into the contributor's team. The main ongoing tasks are all listed on the [roadmap](./roadmap).