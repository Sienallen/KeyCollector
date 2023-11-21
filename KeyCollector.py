import keyboard
import pandas as pd
import os
import string

""" Listens to the keys pressed """
def collectKey():
  while(True):
    
    if(keyboard.read_key()):
      key = keyboard.read_key()
      print(key)
      updateCSV(key)
      if(key == 'q'):
        print('you pressed q')
        break

""" increments the count for the key pressed """
def updateCSV(key):
  file = './CSV/KeyData.csv'
  df = pd.read_csv(file)


  if(not key in df['Letter'].to_list()):
    newRow = [key]
    for i in range(len(df.columns.tolist()) - 1):
      newRow.append(0)
    df.loc[len(df.index.tolist())] = newRow
    
    
  col = df.columns
  index_y = col.get_loc('Presses')
  index = df.index[df['Letter'] == key].to_list() 
  index.append(index_y)


  df.iloc[index[0], index[1]] +=1


  """Updates CSV with new Values"""
  df.to_csv('./CSV/KeyData.csv', index=False)

def printColumn(char):
  file = './CSV/KeyData.csv'
  df = pd.read_csv(file)
  col = df.columns
  index_y = col.get_loc('Presses')
  index = df.index[df['Letter'] == char].to_list() 
  index.append(index_y)
  
  print(f'\nTotal presses for a: {df.iloc[index[0], index[1]]}')



""" Either resets the CSV file to 0 or creates the file if it does not exists """
def defaultCSV():
  letter = {"Letter":[]}

  file = './CSV/KeyData.csv'
  if(os.path.exists(file)):

    for char in string.ascii_lowercase:
      letter["Letter"].append(char)

    data = pd.DataFrame(letter)
    data['Presses'] = 0
    data.to_csv('./CSV/KeyData.csv', index=False)
    
  else:
    data['Presses'] = 0


def printCSV():
  file = './CSV/KeyData.csv'
  df = pd.read_csv(file)
  print(df)


def Menu():
  while(True):
    print("\nMenu")
    print("1. Start the program to read your key inputs.")
    print("2. End the program.")
    print("3. Check how many presses on single character.")
    print("4. Print all the data.")
    print("5. Reset the CSV file to 0.")
    print("9. Exit")
    option = input("Please Enter a Number:")

    match option:
      case '1':
        collectKey()
      case '2':
        print('ending has not been completed')
      case '3':
        char = input("Enter desired letter:")
        printColumn(char)
      case '4':
        printCSV()
      case '5':
        defaultCSV()
      case '9':
        break
      case _ :
        print("Invalid Input.") 


def main():
  Menu()


if __name__ == "__main__":
  main()