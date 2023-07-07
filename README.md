# Bhagavad-Gita
With this program, users can easily search for and retrieve verses from the Bhagavad Gita in different languages(sanskrit, english, hindi, hindi doha) by specifying the chapter number and verse number.

##The program has the following features:

User Interface: The program provides a user interface built using PySimpleGUI, allowing users to input the chapter number and verse number they want to retrieve.

Verse Retrieval: When the user enters the chapter number and verse number and clicks the "Show" button, the program connects to the Bhagavad Gita csv file. It searches for the corresponding chapter and verse file based on the input, and retrieves the shlok in Sanskrit, Hindi, Hindi Doha, and English translations.

Display: The program displays the retrieved shlok in separate sections for Sanskrit, Hindi, Hindi Doha, and English translations. The text is formatted for easy readability.

##Here's a basic outline of the program flow:

Import the necessary libraries, including PySimpleGUI for the user interface.

Create a PySimpleGUI layout for the user interface, including input fields for chapter and verse numbers, a "Search" button, and sections to display the shlok in different languages.

When the "Search" button is clicked, retrieve the chapter and verse numbers entered by the user.

Use the retrieved chapter and verse numbers to connect with gitaF.csv.

Parse the content to extract the shlok in Sanskrit, Hindi, Hindi Doha, and English translations.

Update the corresponding sections in the PySimpleGUI window with the retrieved shlok.

Display the PySimpleGUI window.

##Interface
![image](https://github.com/SHRISTIGUPT/Bhagavad-Gita/assets/91000887/028935bc-7679-49be-9e88-4215db8107f6)

![image](https://github.com/SHRISTIGUPT/Bhagavad-Gita/assets/91000887/12ba3fd7-ed2d-40d4-a15b-1097f4ea2de8)

![image](https://github.com/SHRISTIGUPT/Bhagavad-Gita/assets/91000887/9f96d90d-28d7-4bfe-a23a-5f579750ac60)

![image](https://github.com/SHRISTIGUPT/Bhagavad-Gita/assets/91000887/8d7cdfb1-ffa8-40a2-852f-2a151be48569)

![image](https://github.com/SHRISTIGUPT/Bhagavad-Gita/assets/91000887/92014531-8715-4513-a59b-eadc49218251)
