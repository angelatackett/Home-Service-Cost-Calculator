# Home Service Cost Calculation Program
# This program will determine the price to clean a house or provide yard services determined by user inputs.
# Developer: Angela D. Tackett       CMIS102                            05JUN2022
# Modified : Angela D. Tackett ---- Add Functions/Yard Services         08JUL2022

#function welcome
def WelcomeInputs():
    #Prompt user for name and display service cost options
    print("\n(--------Home Service Cost Calculator-------)\n\n")    
    name = str(input("What is your name? "))
    service = str(input(f'\nWelcome {name.title()}! Are you looking for cleaning or yard services [C or Y]? '))
    #cleaning parameters and validation
    if service == 'C' or service == 'c':
        mow = 0
        edge = 0
        shrub = 0
        print(f'\n\n|--Please take a look at our prices below--|\n')
        # Provide prices to customer
        print('*BASE COST PER HOME SIZE:\n')
        print('    1-4 rooms  : $80')
        print('    5-9 rooms  : $150')
        print('    10 + rooms : $200\n')

        print('*CLEANING OPTIONS:\n')
        print('    QUICK CLEAN : $15 per room')
        print('    DEEP CLEAN  : $25 per room\n')

        print('\n********************Service Descriptions:********************\n\n*QUICK CLEAN : organizing, dusting, vaccuuming, and bed making.\n')
        print('*DEEP CLEANING : quick clean parameters PLUS scrubbing tiles, \nsanitizing surfaces, mopping, windows, laundry, and dishes.\n')
        print('*If there are any tasks outside of the outlined tasks, \nthat will be at the service providers willingness, ability, \npricing, and agreeance with client.\n\n')

        #prompt user for number of rooms, initialize service costs, and prompt for type of service
        no_rooms = eval(input('HOW MANY ROOMS WILL NEED TO BE CLEANED? '))
        for i in range(1000):
            if no_rooms >= 1:
                break
            else:
                print("INVALID INPUT\n")
                no_rooms = eval(input('HOW MANY ROOMS WILL NEED TO BE CLEANED? '))

        #initialize type clean price
        quick_clean = 15
        deep_clean = 25
        #validate
        for i in range(1000):
            type_clean = eval(input('\nWHAT TYPE OF CLEANING IS REQUIRED? \nEnter 1 for QUICK CLEAN \nEnter 2 for DEEP CLEAN: '))
            if type_clean == 1:
                type_clean = quick_clean
                break
            elif type_clean == 2:
                type_clean = deep_clean
                break
            else:
               print("INVALID INPUT\n")
               type_clean = eval(input('\nWHAT TYPE OF CLEANING IS REQUIRED? \nEnter 1 for QUICK CLEAN \nEnter 2 for DEEP CLEAN: '))
                   
    #yard service parameters
    elif service == 'Y' or service == 'y':
        no_rooms = 0
        type_clean = 0
        print(f'\n\n|--Please take a look at our prices below--|\n')

        # Provide prices to customer
        print('*MOWING: $5 PER SQUARE FOOT')
        print('*EDGING: $5 PER PERIMETER FOOT')
        print('*SHRUBS: $5 PER SHRUB\n')
        print('For any service that you do not want included type [0]')
        
        # Prompt user for yard information     
        mow = int(input('\n\nSQUARE FOOTAGE OF YARD: '))
        while True:
            if mow == 0:
                mow = 0
                break
            elif mow < 0:
                print("INVALID INPUT\n")
                mow = int(input('SQUARE FOOTAGE OF YARD: '))
            else:
                break

        edge = int(input('PERIMETER FOOTAGE FOR EDGING: '))
        while True:
            if edge == 0:
                edge = 0
                break
            elif edge < 0:
                print('INVALID INPUT\n')
                edge = int(input('PERIMETER FOOTAGE FOR EDGING: '))
            else:
                break
                
        shrub = int(input('NUMBER OF SHRUBS TO BE PRUNED: '))
        while True:
            if shrub == 0:
                shrub = 0
                break
            elif shrub < 0:
                print('INVALID INPUT\n')
                shrub = int(input('NUMBER OF SHRUBS TO BE PRUNED: '))
            else:
                break
    else:
        service = str(input(f'\nWelcom {name}! Are you looking for cleaning or yard services [C or Y]? '))
    return (name,no_rooms,type_clean,mow,edge,shrub)

#function clean calculation
def Clean(no_rooms,type_clean):
    
    #initialize base room costs
    small = 80
    medium = 150
    large = 200
    clean_quote = 0
    #calculate clean quote
    if no_rooms <= 4 and no_rooms <0:
        clean_quote = small + (no_rooms * type_clean)
    elif 5 <= no_rooms <= 9:
        clean_quote = medium + (no_rooms * type_clean)
    elif no_rooms >= 10:
        clean_quote = large + (no_rooms * type_clean)

    return clean_quote

#function yard calculation
def Yard(mow,edge,shrub):
    #calculate costs
    yard_quote = (mow * 5) + (edge * 5) + (shrub * 5)
    return yard_quote

#display function
def Display(name, clean_quote, yard_quote):


    if clean_quote > 0:
        total_quote = clean_quote
    elif yard_quote > 0:
        total_quote = yard_quote

    #initialize senior discount of 15%
    senior_discount = .15
    senior_disc = total_quote * senior_discount     
    senior = input('\n\nAre you over 65 years old [Y or N]? \n')
    while True:
        if senior == 'Y' or senior == 'y':
            print(f"\n\n--------{name.upper()}'S SERVICE QUOTE---------\n")
            print(f'Service fees: ${total_quote:.2f}')
            print(f'Senior Discount: -${senior_disc:.2f}')
            print(f'Total w/ discount: ${total_quote - senior_disc:.2f}')
            break
        elif senior == 'N' or senior == 'n':
            print(f"\n\n--------{name.upper()}'S SERVICE QUOTE---------\n")
            print(f'Service fees: ${total_quote:.2f}\n')
            print('--------------------------------')
            break
        else:
            print('INVALID INPUT\n')
            senior = input('\n\nAre you over 65 years old [Y or N]? \n')
            
    print('________________________________')
    print('\n**This price does not reflect other fees and taxes.\n\nPlease provide to representative when scheduling.\n')
    print('Thank you and have a wonderful day! :)')

def main():
    name,no_rooms,type_clean,mow,edge,shrub = WelcomeInputs()
    clean_quote = Clean(no_rooms,type_clean)
    yard_quote = Yard(mow,edge,shrub)
    Display(name,clean_quote,yard_quote)

main()
