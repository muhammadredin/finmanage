import streamlit as st


def test():
	def my_function():
		st.title("Streamlit Return Example")
		button_pressed = st.button("Click me")

		if button_pressed:
			# Inject custom HTML and CSS
			st.markdown(
				"""
				<style>
				.notification {
					position: fixed;
					top: 52px;
					right: 12px;
					background-color: yellow;
					padding: 12px;
					border-radius: 5px;
					animation: fade-out 3s forwards;
					color:black;
				}

				@keyframes fade-out {
					0% {
						opacity: 1;
					}
					100% {
						opacity: 0;
					}
				}
				</style>
				""",
				unsafe_allow_html=True
			)
			def show_notification(message):
				st.markdown(f"<div class='notification'>{message}</div>", unsafe_allow_html=True)

			# Example usage
			show_notification("This is a notification message.")
			return "Button was clicked!"
		else:
			return "Button was not clicked."

	result = my_function()
	st.write(result)