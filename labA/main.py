from sys import stdin
import re

PATTERN = '\d+|\s'

class Customer:
  def __init__(self, cash, time):
      self.cash = cash
      self.time = time      


def insertCash(q, customer):
  while customer.time >= 0:
    if q[customer.time] == 0:
      q[customer.time] = customer.cash
      return
    customer.time -= 1
  
def calculateCash(q, sortedCash):
  bankIsOpen      = True
  customersInLine = len(sortedCash)
  servedCustomer  = 0
  while bankIsOpen:
    if servedCustomer < customersInLine:
      insertCash(q, sortedCash[servedCustomer])
      servedCustomer += 1
    else: bankIsOpen = False
  return

def main():
  fstInput                     = stdin.readline()
  listOfFstInput               = re.findall(PATTERN, fstInput)
  customers, timeTilClose      = int(listOfFstInput[0]), int(listOfFstInput[2])
  listOfCustomers              = []
  q                            = [0 for i in range(timeTilClose)]    
  while customers > 0:
    sndInput       = stdin.readline()
    listOfSndInput = re.findall(PATTERN, sndInput)
    cash, time     = int(listOfSndInput[0]), int(listOfSndInput[2])
    listOfCustomers.append(Customer(cash, time))
    customers -= 1
  sortedCash = sorted(listOfCustomers,
                      key=lambda customer: customer.cash, reverse=True)
  calculateCash(q, sortedCash)
  total = 0
  for i in range(len(q)): total += q[i]  
  print (total)


if __name__ == '__main__':
    main()  

