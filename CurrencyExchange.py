#import external libraries used in code
import requests, json
import pycountry

print('Currency Exchange')

currencies = []

def findCurrency():
    #Finds all avaliable currencies
    allCurrency = (list(pycountry.currencies))
    for x in allCurrency:
        y = str(x)
        y = y[18:21]
    #Adds the value of their ISO to the "currencies" list
        currencies.append(y)
    #Organizes all values in "currency" list
    currecyDisplay = ''
    inline = 0
    for cs in currencies:
        currecyDisplay += cs + ' | '
        inline += 1
        #Allows up to 26 ISOs to be in one line
        if inline >= 26:
            currecyDisplay += '\n '
            inline = 0
    #Displays all currency ISOs to user
    print('Avaliable Currencies:\n',currecyDisplay)

def help():
      #Ask user if they need help
      questions = input('Type ? for help or Enter to continue: ')
      #If user inputs "?" run help procedure
      if questions == '?':
            #Display information order
            print('--------\nCurrency Exchange Help\nISO currency codes are three-letter alphabetic codes that represent the various currencies\n\nCurrency ISO:\nCurrency Name:\n--------')
            #Obtains information of all currencies
            allCurrency = (list(pycountry.currencies))
            #For each currency obtain the ISO and the name of currency
            #Display ISO and Data
            for x in allCurrency:
                  y = str(x)
                  w = y[18:21]
                  n = int(y.index(',', y.index(',') + 1))
                  z = y[30:n-1]
                  print(w)
                  print(z + '\n')
            print('--------\n')
    #Else user does not input "?" continue program
      else:
            pass

def userInput():
    #Program try asking user for data input
    try:
        fromCurrency = input('From (ISO): ').upper()
        toCurrency = input('To (ISO): ').upper()
        currencyAmount  = input('Amount: ')
        currencyAmount = int(currencyAmount.replace(',', ''))
    #If data inputed is not the correct type of data inform user
    except ValueError:
        print('Amount Is A Number Value')
    #Return inputed data
    return currencyAmount, fromCurrency, toCurrency

def checkInfo(fromC, toC, currencyA, check):
    #"validCurrency" value increses as data inputed if verified
    validCurrency = 0
    #Check if inputed ISO is valid
    #If values are valid the vlue of "validCurrency" is increased
    for givenCurrencies in currencies:
        if fromC == givenCurrencies:
            validCurrency += 1
    for givenCurrencies in currencies:
        if toC == givenCurrencies:
            validCurrency += 1
    #Check if "validCurrency" meets necessary verification value
    #Check if "validCurrency" is not 2 (Data is not valid) or inputed amount data is not the correct value
    if validCurrency != 2 or type(currencyA) != int:
        #Let user know data is invalid
        print('Information Invalid\n')
        #Ask user if they need help
        help()
        #Reset "validCurrency"
        validCurrency = 0
        #Set "check" as False
        checks = False
    #If type of data is correct and valid "check" is set to True
    else:
        checks = True
    return fromC, toC, currencyA, checks

def dataInput():
    #Data has not been checked yet, therefore "check" is False
    check = False
    #While the data is not valid or not checked repeat data input and data check
    while check == False:
        currencyAmount, fromCurrency, toCurrency = userInput()
        fromC, toC, currencyA, check = checkInfo(fromCurrency, toCurrency, currencyAmount, check)
    #Once data is valid and checked return values
    return fromC, toC, currencyA

def userData():
    #No data if the information provided is correct
    correctInfo = ''
    #While the user does not approve of data, repeat data input and data check
    while correctInfo != 'y':
        fromC, toC, currencyA = dataInput()
        #Display data user has inputed after being checked and validated
        print('\nFrom:',fromC)
        print('To:',toC)
        print('Amount:', currencyA)
        #Ask user if the data provided is correct
        correctInfo = input('Is the information correct (y/n)?: ').lower()
        print('')
        help()
    #Once data is approved by user, return values
    return currencyA, fromC, toC

def realTimeRate(from_currency, to_currency):
    #API key provided by Alpha Vanatage
    api_key = "1RU6IZY5D9UIISJK"
    #Define "url" where data is stored
    #"url" varies from user selected data
    url = ('https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=%s&to_currency=%s&apikey=%s' % (from_currency, to_currency, api_key))
    #Get response from reqest of "url"
    req = requests.get(url)
    #Obtain json format and set data for python to read
    #"Result" has nested dictionaries
    result = req.json() 
    #Display exchange rate information to user
    print("Realtime Currency Exchange Rate for", 
          result["Realtime Currency Exchange Rate"] 
                ["2. From_Currency Name"], "to", 
          result["Realtime Currency Exchange Rate"] 
                ["4. To_Currency Name"], "is", 
          result["Realtime Currency Exchange Rate"] 
                ['5. Exchange Rate'], to_currency) 
    #Return the value of exchange
    return float(result["Realtime Currency Exchange Rate"] 
    ['5. Exchange Rate'])

def completeExchange(rate, cAmount, fCurrency, tCurrency):
    #Total of the "to" currency is the rate times the amount of the "from" currency
    total = rate * cAmount
    end = ' '
    #Maintain program Running until user has inputed the Enter key
    while end == ' ':
        print('\n%s %s is %.2f %s' % (cAmount, fCurrency, total, tCurrency))
        end = input('Press Enter To Close')
    

if __name__ == "__main__":
    findCurrency()
    help()
    currencyAmount, fromCurrency, toCurrency = userData()
    rate = realTimeRate(fromCurrency, toCurrency)
    completeExchange(rate, currencyAmount, fromCurrency, toCurrency)


