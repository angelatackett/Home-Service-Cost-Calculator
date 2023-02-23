# Home Service Cost Calculator

The code provided is a home service cost calculator that allows customers to select between cleaning and yard services. The program asks for the customer's name and what type of service they require. It then displays the pricing options for the selected service, prompts the user for required inputs, and calculates the quote based on the provided inputs.

The program is structured into three functions: 

'WelcomeInputs()', 'Clean()', 'Yard()', and 'Display()'.

- WelcomeInputs() prompts the user for their name and type of service. It then displays pricing options and prompts the user for required inputs based on the selected service. It returns a tuple with the required inputs.
- Clean() takes in the number of rooms and the type of cleaning required and calculates the cost of cleaning. It returns the calculated quote.
- Yard() takes in the yard size, perimeter footage for edging, and number of shrubs to be pruned and calculates the cost of yard service. It returns the calculated quote.
- Display() takes in the customer's name, the calculated cleaning quote, and the calculated yard quote. It displays the customer's name and the total cost of the selected service.

The code could be improved by including error handling for invalid inputs, allowing for more flexible pricing options, and adding more services.
