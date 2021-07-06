
import pandas as pd
#This will downsize the data and split it into a 70-30 training testing split. It is made to be executed in the same directory as
#the CheXpert small dataset. (more documentation to be added)

def downsizeDataset(downsizeRatio, train, valid):
    num_new_train = (int)(len(train.index)*downsizeRatio)
    num_new_valid = (int)(len(valid.index)*downsizeRatio)
    train = train.head(num_new_train)
    valid = valid.head(num_new_valid)
    return train, valid
def splitTestTrain(percentTest, train):
    num_test = (int)(percentTest*len(train.index))
    num_train = len(train.index)-num_test
    train = train.head(num_train)
    test = train.tail(num_test)
    print(num_test)
    return test, train
def exportAll(test, train, valid):
    train.to_csv("CheXpert-v1.0-small/train.csv")
    valid.to_csv("CheXpert-v1.0-small/valid.csv")
    test.to_csv("CheXpert-v1.0-small/test.csv")
    print("exported!")
originalTrain = pd.read_csv("/gpfs/data/huo-lab/Image/rachnagupta/CovidPrognosis/CheXpert/CheXpert-v1.0-small/train_original.csv")
originalValid = pd.read_csv("/gpfs/data/huo-lab/Image/rachnagupta/CovidPrognosis/CheXpert/CheXpert-v1.0-small/valid_original.csv")
train, valid = downsizeDataset(0.3, originalTrain, originalValid)
test, train = splitTestTrain(0.7, train)
exportAll(test, train, valid)
