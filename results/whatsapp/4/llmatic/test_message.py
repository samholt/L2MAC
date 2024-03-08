def test_message():
	message = Message("Hello, world!", "Alice", "Bob")

	assert message.content == "Hello, world!"
	assert message.sender == "Alice"
	assert message.receiver == "Bob"
	assert message.read == False

	message.handle_text("Hello, world!")
	assert message.content == "Hello, world!"

	message.handle_image("image.jpg")
	assert message.content == "image.jpg"

	message.handle_emoji(":smile:")
	assert message.content == ":smile:"

	message.handle_gif("funny.gif")
	assert message.content == "funny.gif"

	message.handle_sticker("cool.sticker")
	assert message.content == "cool.sticker"
