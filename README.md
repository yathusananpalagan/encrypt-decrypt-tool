# Encrypt and Decrypt Tool 🔐📝
**Encrypt and Decrypt Tool** is a Python-based GUI application that allows users to securely encrypt and decrypt text using shift-based (Caesar-style) ciphers. Built with `customtkinter`, it provides a clean and intuitive interface for transforming messages using both numeric and text-based shift keys, while offering real-time history tracking, theme toggling, and export capabilities.

## 🚀 Key Features

- 🔁 **Text Encryption & Decryption**: Encrypt or decrypt messages using a shift cipher with ease.
- 🔢 **Flexible Shift Input**: Supports both numeric shifts (e.g., 3) and alphabetic keys (e.g., "abc"), enabling multi-shift encryption.
- 🖥️ **Modern GUI**: Built with `customtkinter` for a user-friendly and visually appealing interface. 
- 📋 **Clipboard Support**: Instantly copy results with a single click for use elsewhere.
- 🌙 **Dark/Light Mode Toggle**: Seamlessly switch between dark and light themes for better visibility.
- 🧠 **Action History**: Automatically logs all encryption and decryption actions with timestamps.
- 🔍 **Searchable Log**: Filter history entries in real-time by message content or result.
- 💾 **Export Options**: Save the full action history as `.txt` and `.csv` files for reference or analysis.
- 🚫 **Input Validation**: Detects and displays user-friendly error messages for invalid inputs.
- 🔒 **Read-Only Output Fields**: Prevents unintentional edits to encrypted/decrypted results.
- 🧰 **Tabbed Layout**: Organized interface with separate tabs for Encrypt, Decrypt, and History views.

## 🛠️ Tools & Technologies

[![Technologies](https://skillicons.dev/icons?i=git,github,vscode,py,md,windows)](https://skillicons.dev)

## 📂 Project Structure
Here are some important files in the project structure:
- [**encrypt-decrypt-tool.py**](./encrypt-decrypt-tool.py): The main Python script that runs the tool
- [**requirements.txt**](./requirements.txt): A text file containing a list of required Python libraries to run the project
- [**README.md**](./README.md): This documentation file, which explains the project and how to use it.
- [**out/**](./out): Directory containing history logs for encryption and decryption operations.
- [**history.csv**](./out/history.csv): CSV file storing logs of operations (message, result, timestamp).
- [**history.txt**](./out/history.txt): Text file with a readable log of operations, including timestamps and results.


## 🔧 Installation

### 📝 Things Needed:

Before you begin, make sure you have the following installed on your system:
- **Python 3.x** (You can download it from [python.org](https://www.python.org/downloads/))
- **Git** (To clone the repository)

### 📦 Steps to Install:
1. **Clone the Repository**  
   First, clone the repository using Git. Open your terminal or command prompt and run the following command:
   
   ```bash
   git clone https://github.com/yathusananpalagan/encrypt-decrypt-tool.git
   ```
2. **Navigate to the Project Folder**
   Once the repository is cloned, navigate to the project directory:
   
   ```bash
   cd encrypt-decrypt-tool
   ```
4. **Install Dependencies**
   The project requires some Python libraries to work. You can install all the dependencies listed in the [`requirements.txt`](./requirements.txt) file using pip:
   ```bash
   pip install -r requirements.txt
   ```
   
## ▶️ Usage

### 1. **Starting the Application**

Navigate to the project directory (if not already there) and run the [`encrypt-decrypt-tool.py`](./encrypt-decrypt-tool.py) script:

```bash
python encrypt-decrypt-tool.py
```
This will launch the GUI where you can interactively choose to encrypt or decrypt messages using a custom key.

### 2. **Encrypting Text**
- In the GUI, select the "Encrypt" option.
- Enter the text you want to encrypt in the input field.
- Provide a secret key that will be used for the encryption process.
- Click the "Encrypt" button.
- The encrypted text will be displayed and can be copied or saved for later use.

### 3. **Decrypting Text**
- Choose the "Decrypt" option in the GUI.
- Paste or type the previously encrypted text.
- Enter the same secret key used during encryption.
- Click the "Decrypt" button to retrieve the original message.
- If the key is incorrect, the output may be unreadable or trigger an error.

### 4. **Key Management Tips**
- Use a strong and memorable key for encryption and decryption.
- The same key must be used for both operations to correctly retrieve the original text.
- Do not share your encryption key publicly to ensure the confidentiality of your messages.

### 5. **Optional Enhancements**
- You can modify or extend the tool to support saving encrypted/decrypted messages to a file.
- Support for additional encryption algorithms (e.g., AES, Fernet) can also be added for advanced users.

> 🔐 This tool is ideal for simple message protection and learning purposes. For sensitive or critical data, consider using standardized encryption libraries and practices.

## 🖼️ Screenshots
### Encrypt Tab

### Decrypt Tab

### History Tab

## 📜 License
This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## 🤝 Contributions

Contributions are always welcome! If you'd like to contribute to this project, feel free to submit a pull request or open an issue. Your help is greatly appreciated! 😊

## 📬 Contact

If you have any questions, feedback, or suggestions, feel free to reach out to me:

- **GitHub**: [@YathusanAnpalagan](https://github.com/yathusananpalagan)
- **LinkedIn**: [@YathusanAnpalagan](https://www.linkedin.com/in/yathusan-anpalagan-805957353/)

I'm happy to help and would love to hear your thoughts! 😊

## 🌟 Show Your Support

If you found this project useful or interesting, please consider giving it a **star** on GitHub! ⭐
<br>
Thank you for your support! 🙏

## 📚 Libraries Used

This project utilizes the following Python libraries:

- **customtkinter**: Used to create a graphical user interface (GUI) for the Encrypt and Decrypt Tool, providing an interactive and visually appealing interface.
- **tkinter**: The standard Python interface to the Tk GUI toolkit.
- **datetime**: Used to track and log timestamps for encryption and decryption operations.
- **os**: Used for interacting with the operating system, including creating directories and managing file paths.
