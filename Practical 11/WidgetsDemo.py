# Import all definitions from tkinter
from tkinter import * 

class WidgetsDemo:
    def __init__(self):
        # Create a window and set a title
        window = Tk() 
        window.title("Widgets Demo") 

        # Create and add a frame to window
        frame1 = Frame(window) 
        frame1.pack()
        
        # Create two variables to associate them with check and radio buttons 
        self.v1 = IntVar()
        self.v2 = IntVar()
        
        # Create a check button and add it to frame1
        cbtBold = Checkbutton(frame1, text = "Bold", variable = self.v1, 
                              command = self.processCheckbutton) 
        
        # Create two radio buttons and add them to frame1
        rbRed = Radiobutton(frame1, text = "Red", bg = "red", 
                            variable = self.v2, value = 1, 
                            command = self.processRadiobutton) 
        rbYellow = Radiobutton(frame1, text = "Yellow", bg = "yellow", 
                               variable = self.v2, value = 2, 
                               command = self.processRadiobutton)

        # Organize check and radio buttons in frame1 using grid manager
        cbtBold.grid(row = 1, column = 1) 
        rbRed.grid(row = 1, column = 2)
        rbYellow.grid(row = 1, column = 3)
        
        # Create and add another frame to window
        frame2 = Frame(window) 
        frame2.pack()

        # Create a label, an entry and a button and add them to frame2
        label = Label(frame2, text = "Enter your name: ")
        self.name = StringVar()
        entryName = Entry(frame2, textvariable = self.name)
        btGetName = Button(frame2, text = "Get Name", 
                           command = self.processButton)
        message = Message(frame2, text = "It is a widgets demo")

        # Organize the label, entry and button in frame2 using grid manager
        label.grid(row = 1, column = 1)
        entryName.grid(row = 1, column = 2)
        btGetName.grid(row = 1, column = 3)
        message.grid(row = 1, column = 4)

        # Add text
        text = Text(window) # Create and add text to the window
        text.pack()
        text.insert(END, "Tip\nThe best way to learn Tkinter is to read ")
        text.insert(END, "these carefully designed examples and use them ")
        text.insert(END, "to create your applications.")
        
        # Create an event loop
        window.mainloop()

    # Invoke the processCheckbutton method when the check button is clicked 
    def processCheckbutton(self):
        print("check button is " + 
              ("checked " if self.v1.get() == 1 else "unchecked"))

    # Invoke the processRadiobutton method when the radio button is clicked
    def processRadiobutton(self):
        print(("Red" if self.v2.get() == 1 else "Yellow") + " is selected " )
    
    # Invoke the processButton method when the GetName is clicked
    def processButton(self):
        print("Your name is " + self.name.get())

# Create GUI 
WidgetsDemo()
