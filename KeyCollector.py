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



def addKeyToCSV(key):
  data = pd.read_csv('./CSV/KeyData.csv')
  pass


def main():
  file = './CSV/KeyData.csv'
  """ collectKey()
  updateCSV('a') """
  if(os.path.exists(file)):
    print("file exists")
    """ collectKey() """
    """ updateCSV("a") """
    pass
  else:
    defaultCSV()
  defaultCSV()


if __name__ == "__main__":
  main()