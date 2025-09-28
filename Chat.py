# Python & HTML Learning Chatbot
# A rule-based chatbot that answers questions about Python programming and HTML
# Created for educational purposes

def programming_chatbot():
    """
    A rule-based chatbot that helps users learn Python programming and HTML concepts
    """
    
    print("Welcome to CodeBot - Your Programming Learning Assistant!")
    print("I can help you with Python programming and HTML questions.")
    print("Type 'quit', 'exit', or 'bye' to end our conversation.\n")
    
    # Main conversation loop
    while True:
        user_input = input("You: ").strip().lower()
        
        # Exit conditions
        if user_input in ['quit', 'exit', 'bye', 'goodbye']:
            print("CodeBot: Thanks for learning with me! Happy coding!")
            break
        
        # Empty input handling
        if not user_input:
            print("CodeBot: Please ask me something about Python or HTML!")
            continue
        
        # Greetings
        if any(greeting in user_input for greeting in ['hello', 'hi', 'hey', 'greetings']):
            print("CodeBot: Hello! I'm here to help you learn Python and HTML. What would you like to know?")
        
        # === HTML CONCEPTS ===
        
        # HTML basics
        elif any(word in user_input for word in ['what is html', 'html language', 'about html']):
            print("CodeBot: HTML (HyperText Markup Language) is the standard markup language")
            print("        for creating web pages. It describes the structure and content of")
            print("        web pages using tags and elements!")
        
        # HTML structure
        elif any(word in user_input for word in ['html structure', 'html document', 'basic html']):
            print("CodeBot: Basic HTML document structure:")
            print("        <!DOCTYPE html>")
            print("        <html>")
            print("        <head>")
            print("            <title>Page Title</title>")
            print("        </head>")
            print("        <body>")
            print("            <h1>My First Heading</h1>")
            print("            <p>My first paragraph.</p>")
            print("        </body>")
            print("        </html>")
        
        # HTML tags
        elif any(word in user_input for word in ['html tags', 'tags', 'elements']):
            print("CodeBot: HTML tags are keywords surrounded by angle brackets:")
            print("        • <h1> to <h6> - Headings (largest to smallest)")
            print("        • <p> - Paragraphs")
            print("        • <a> - Links")
            print("        • <img> - Images")
            print("        • <div> - Divisions/containers")
            print("        • <span> - Inline containers")
        
        # HTML attributes
        elif any(word in user_input for word in ['html attributes', 'attributes']):
            print("CodeBot: HTML attributes provide additional information about elements:")
            print("        • id='unique-identifier' - Unique identifier")
            print("        • class='style-class' - CSS class for styling")
            print("        • src='image.jpg' - Source for images/media")
            print("        • href='https://example.com' - Link destination")
            print("        • alt='description' - Alternative text for images")
        
        # HTML headings
        elif any(word in user_input for word in ['heading', 'headings', 'h1', 'h2']):
            print("CodeBot: HTML headings define the hierarchy of content:")
            print("        <h1>Main Title</h1>        <!-- Most important -->")
            print("        <h2>Section Title</h2>     <!-- Second level -->")
            print("        <h3>Subsection</h3>        <!-- Third level -->")
            print("        ... up to <h6> for smallest headings")
        
        # HTML links
        elif any(word in user_input for word in ['link', 'links', 'anchor']):
            print("CodeBot: HTML links connect pages and resources:")
            print("        <a href='https://example.com'>Visit Example</a>")
            print("        <a href='page.html'>Internal link</a>")
            print("        <a href='mailto:email@example.com'>Send Email</a>")
            print("        <a href='#section'>Jump to section</a>")
        
        # HTML images
        elif any(word in user_input for word in ['image', 'images', 'img']):
            print("CodeBot: HTML images are embedded using the <img> tag:")
            print("        <img src='photo.jpg' alt='Description' width='300' height='200'>")
            print("        • src - path to image file")
            print("        • alt - alternative text for accessibility")
            print("        • width/height - dimensions (optional)")
        
        # HTML lists
        elif any(word in user_input for word in ['html list', 'lists', 'ul', 'ol']):
            print("CodeBot: HTML has two types of lists:")
            print("        Unordered list (bullets):")
            print("        <ul>")
            print("          <li>Item 1</li>")
            print("          <li>Item 2</li>")
            print("        </ul>")
            print("        ")
            print("        Ordered list (numbers):")
            print("        <ol>")
            print("          <li>First item</li>")
            print("          <li>Second item</li>")
            print("        </ol>")
        
        # HTML forms
        elif any(word in user_input for word in ['form', 'forms', 'input']):
            print("CodeBot: HTML forms collect user input:")
            print("        <form action='submit.php' method='post'>")
            print("          <input type='text' name='username' placeholder='Username'>")
            print("          <input type='password' name='password' placeholder='Password'>")
            print("          <input type='email' name='email' placeholder='Email'>")
            print("          <button type='submit'>Submit</button>")
            print("        </form>")
        
        # HTML tables
        elif any(word in user_input for word in ['table', 'tables']):
            print("CodeBot: HTML tables display data in rows and columns:")
            print("        <table>")
            print("          <tr>")
            print("            <th>Name</th>")
            print("            <th>Age</th>")
            print("          </tr>")
            print("          <tr>")
            print("            <td>John</td>")
            print("            <td>25</td>")
            print("          </tr>")
            print("        </table>")
        
        # CSS in HTML
        elif any(word in user_input for word in ['css', 'styling', 'style']):
            print("CodeBot: CSS styles HTML elements. Three ways to add CSS:")
            print("        1. Inline: <p style='color: blue;'>Blue text</p>")
            print("        2. Internal: <style>p {color: blue;}</style> in <head>")
            print("        3. External: <link rel='stylesheet' href='styles.css'>")
        
        # === PYTHON CONCEPTS (keeping existing ones) ===
        
        # Python basics
        elif any(word in user_input for word in ['what is python', 'python language', 'about python']):
            print("CodeBot: Python is a high-level, interpreted programming language known for its")
            print("         simple syntax and readability. It's great for beginners and widely used")
            print("         in web development, data science, AI, and automation!")
        
        # Variables
        elif any(word in user_input for word in ['variable', 'variables']) and 'html' not in user_input:
            print("CodeBot: Variables in Python store data values. You don't need to declare their type.")
            print("         Example: name = 'John', age = 25, height = 5.8")
            print("         Python automatically determines the data type!")
        
        # Data types
        elif any(word in user_input for word in ['data type', 'data types', 'types']) and 'html' not in user_input:
            print("CodeBot: Python has several built-in data types:")
            print("         • Text: str (string)")
            print("         • Numeric: int (integer), float (decimal), complex")
            print("         • Sequence: list, tuple, range")
            print("         • Boolean: bool (True/False)")
            print("         • Set: set, frozenset")
            print("         • Mapping: dict (dictionary)")
        
        # Lists
        elif 'list' in user_input and 'html' not in user_input:
            print("CodeBot: Lists are ordered collections that can hold different data types.")
            print("         Example: my_list = [1, 2, 'hello', True]")
            print("         Lists are mutable (changeable) and support indexing!")
        
        # Dictionaries
        elif any(word in user_input for word in ['dictionary', 'dict']):
            print("CodeBot: Dictionaries store key-value pairs and are unordered collections.")
            print("         Example: student = {'name': 'Alice', 'age': 20, 'grade': 'A'}")
            print("         Access values using keys: student['name'] returns 'Alice'")
        
        # Functions
        elif 'function' in user_input and 'html' not in user_input:
            print("CodeBot: Functions are reusable blocks of code. Define them with 'def':")
            print("         def greet(name):")
            print("             return f'Hello, {name}!'")
            print("         Call it: greet('Alice') returns 'Hello, Alice!'")
        
        # Loops
        elif 'loop' in user_input:
            print("CodeBot: Python has two main types of loops:")
            print("         • for loop: for item in sequence")
            print("         • while loop: while condition is True")
            print("         Example: for i in range(5): print(i)  # prints 0 to 4")
        
        # If statements
        elif any(word in user_input for word in ['if statement', 'conditional', 'if-else']):
            print("CodeBot: Conditional statements control program flow:")
            print("         if condition:")
            print("             # do something")
            print("         elif another_condition:")
            print("             # do something else")
            print("         else:")
            print("             # default action")
        
        # Print statement
        elif 'print' in user_input:
            print("CodeBot: print() function displays output to the console.")
            print("         Example: print('Hello World!')")
            print("         You can print variables: print(f'My name is {name}')")
        
        # Input statement
        elif 'input' in user_input and 'html' not in user_input:
            print("CodeBot: input() function gets user input as a string.")
            print("         Example: name = input('Enter your name: ')")
            print("         Convert to other types: age = int(input('Enter age: '))")
        
        # Comments
        elif 'comment' in user_input:
            print("CodeBot: Comments explain code and are ignored during execution:")
            print("         # This is a single-line comment")
            print("         '''This is a")
            print("         multi-line comment'''")
        
        # Indentation
        elif 'indentation' in user_input:
            print("CodeBot: Python uses indentation (spaces/tabs) to define code blocks.")
            print("         Unlike other languages, Python doesn't use {} braces.")
            print("         Standard is 4 spaces per indentation level.")
        
        # Libraries/modules
        elif any(word in user_input for word in ['library', 'module', 'import']):
            print("CodeBot: Import libraries to extend Python's functionality:")
            print("         import math  # imports entire module")
            print("         from random import randint  # imports specific function")
            print("         Popular libraries: numpy, pandas, matplotlib, requests")
        
        # Error handling
        elif any(word in user_input for word in ['error', 'exception', 'try-except']):
            print("CodeBot: Handle errors gracefully with try-except blocks:")
            print("         try:")
            print("             result = 10 / 0")
            print("         except ZeroDivisionError:")
            print("             print('Cannot divide by zero!')")
        
        # String methods
        elif 'string' in user_input:
            print("CodeBot: Strings have many useful methods:")
            print("         • .upper() - converts to uppercase")
            print("         • .lower() - converts to lowercase")
            print("         • .split() - splits into a list")
            print("         • .replace() - replaces text")
            print("         Example: 'hello'.upper() returns 'HELLO'")
        
        # File handling
        elif 'file' in user_input:
            print("CodeBot: Handle files with open() function:")
            print("         with open('file.txt', 'r') as f:")
            print("             content = f.read()")
            print("         Modes: 'r' (read), 'w' (write), 'a' (append)")
        
        # Classes and OOP
        elif any(word in user_input for word in ['class', 'object', 'oop']):
            print("CodeBot: Object-Oriented Programming with classes:")
            print("         class Dog:")
            print("             def __init__(self, name):")
            print("                 self.name = name")
            print("             def bark(self):")
            print("                 return f'{self.name} says woof!'")
        
        # Help command
        elif 'help' in user_input:
            print("CodeBot: I can help with these topics:")
            print("         ")
            print("         PYTHON:")
            print("         • Python basics and syntax")
            print("         • Variables and data types")
            print("         • Lists, dictionaries, and other data structures")
            print("         • Functions and loops")
            print("         • Conditional statements (if-else)")
            print("         • Print and input statements")
            print("         • Comments and indentation")
            print("         • Libraries and modules")
            print("         • Error handling")
            print("         • String methods")
            print("         • File handling")
            print("         • Classes and OOP")
            print("         ")
            print("         HTML:")
            print("         • HTML basics and structure")
            print("         • HTML tags and elements")
            print("         • Attributes and properties")
            print("         • Headings, paragraphs, and text")
            print("         • Links and images")
            print("         • Lists and tables")
            print("         • Forms and input elements")
            print("         • CSS styling basics")
        
        # Default response for unrecognized input
        else:
            responses = [
                "I'm not sure about that. Can you ask about Python or HTML concepts?",
                "That's interesting! Try asking me about Python syntax, HTML tags, or programming concepts.",
                "I specialize in Python and HTML. Ask me about variables, functions, HTML structure, or web development!",
                "Hmm, I don't understand that. Type 'help' to see what I can assist you with!"
            ]
            import random
            print(f"CodeBot: {random.choice(responses)}")

# Run the chatbot
if __name__ == "__main__":
    programming_chatbot()
