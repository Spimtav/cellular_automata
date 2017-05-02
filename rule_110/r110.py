# -*- coding: utf-8 -*-
#r110.py
#Maximillian Tinati (mrt59)
#April 5, 2016
"""Module to simulate Wolfram's Rule 110."""

RULE_MAP= {"111":0, "110":1, "101":1, "100":0, "011":1, "010":1, "001":1,
          "000":0}
STARTING_ROW= [1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1]
ROW_LEN= 100     #pls be even
NUM_ITERATIONS= 1000


def genStartingRow():
  """Returns: the starting row, with padding on left side until ROW_LEN."""
  startRow= [0]*(ROW_LEN-len(STARTING_ROW)-1)
  startRow.extend(STARTING_ROW)
  startRow.append(0)
  print startRow
  return startRow


def nextCell(left, mid, right):
  """Calculates the value of the cell below mid, based on Wolfram's 
       Rule 110.
     Returns: 0 or 1.
     Precondition: left, mid, right are 0 or 1."""
  return RULE_MAP["%d%d%d" % (left, mid, right)]


def nextRow(row):
  """Calculates the next row in the pattern based on the input row.
       Assumes left and right terminal cells are padded by 0's.
       This implies that row length grows by 2 each time.
     Returns: list containing the next row of the automaton.
     Precondition: row is a list of 0's and 1's."""
  paddedRow= row[:]
  paddedRow.insert(0,0)
  paddedRow.insert(0,0)
  paddedRow.append(0)
  paddedRow.append(0)
  print paddedRow
  n= []
  for i in range(1, len(paddedRow)-1):
    n.append(nextCell(paddedRow[i-1], paddedRow[i], paddedRow[i+1]))
  return n


def nextRowNoWrapping(row):
  """Calculates the next row, while ignoring edge nodes.i
     Returns: list containing the next row of the automaton.
     Precondition: row is a list of 0's and 1's."""
  n= []
  for i in range(1, len(row)-1):
    n.append(nextCell(row[i-1], row[i], row[i+1]))
  n.insert(0,0)
  n.append(0)
  return n


def runAutomata(iterations):
  """Returns: list of <iterations> rows, where row i is parent of row i+1.
     Precondition: iterations is the number of rows desired."""
  rows= [genStartingRow()]
  for i in range(iterations):
    rows.append(nextRowNoWrapping(rows[i]))
  return rows


def printRows(rows):
  """Prints the rows of the automata, with left alignment (simplicity).
     Precondition: rows is a list of list of 0's and 1's."""
  for i in rows:
    rowCopy= map(lambda x : " " if x == 0 else "█", i[:])
    print " ".join(rowCopy)
    

if __name__ == "__main__":
  rows= runAutomata(NUM_ITERATIONS)
  printRows(rows)









