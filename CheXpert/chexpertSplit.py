
import pandas as pd
#This will downsize the data and split it into a 70-30 training testing split. It is made to be executed in the same directory as
#the CheXpert small dataset. (more documentation to be added)
NUM_PATIENTS_IN_TRAIN = 64740
def downsizeDataset(downsizeRatio, train, valid):
    num_new_train = (int)(len(train.index)*downsizeRatio)
    num_new_valid = (int)(len(valid.index)*downsizeRatio)
    train = train.head(num_new_train)
    valid = valid.head(num_new_valid)
    return train, valid
def splitTestTrain(percentTest, train):
    num_test = (int)(percentTest*NUM_PATIENTS_IN_TRAIN)
    num_train = NUM_PATIENTS_IN_TRAIN-num_test
    selected_columns = train[['Path']]
    selected_columns["Path"] = selected_columns["Path"].str[33:]
    selected_columns["Path"] = selected_columns["Path"].str[:5]
    patient_id = str(num_train)
    indexes = selected_columns.index[selected_columns["Path"]==patient_id].tolist()
    test = train.tail(len(train.index)-indexes[-1])
    train = train.head(indexes[-1])
    print(len(train.index))
    print(len(test.index))
    print(len(valid.index))
    return test, train
def exportAll(test, train, valid):
    train.to_csv("CheXpert-v1.0-small/train.csv")
    valid.to_csv("CheXpert-v1.0-small/valid.csv")
    test.to_csv("CheXpert-v1.0-small/test.csv")
    print("exported!")
originalTrain = pd.read_csv("/gpfs/data/huo-lab/Image/rachnagupta/CovidPrognosis/CheXpert/CheXpert-v1.0-small/train_original.csv")
originalValid = pd.read_csv("/gpfs/data/huo-lab/Image/rachnagupta/CovidPrognosis/CheXpert/CheXpert-v1.0-small/valid_original.csv")
valid = originalValid
train = originalTrain
test, train = splitTestTrain(0.3, train)
exportAll(test, train, valid)