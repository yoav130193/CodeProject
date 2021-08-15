# This is a sample Python script.

# Press ⇧F10 to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from Utils.numphyExamples import numphyExamples
from Utils.pandasExamples import pandasExamples


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.
    nump = numphyExamples()
    # nump.four()
    # nump.five()
    # nump.six()
    # nump.eight()
    # nump.thirteen()
    # nump.function()
    # nump.plot()
    pand = pandasExamples()
    pand.second()
    # pand.one()

    # pand.seriesExamples()
    # pand.dataFramesExamples()
    #pand.readFiles()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
