import io

import pandas as pd  # DataFrame, Series
import pydotplus
from matplotlib import pyplot as plt
from scipy import misc
# from IPython.display import display # for displaying the data
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

# Reading the data
data = pd.read_csv(r'productive_bandwidth_allocation\users\data\users.csv', header=None, index_col=False, names=['dept',
                                                                                                                 'is_student',
                                                                                                                 'age',
                                                                                                                 'grp'])

# It is used for One-Hot encoding
data_dummies = pd.get_dummies(data)

# ID3 Decision Tree algorithm has been used criterion="entropy"
c = DecisionTreeClassifier(criterion="entropy")

# features = data_dummies.ix[:, 'is_student', 'age', 'dept_COMPS', 'dept_Extc']  for indexing this lined has been used
# print(data_dummies.columns)


# selecting all the columns for features except grp which is a label
new = data_dummies.ix[:]
new.pop('grp')
new_features_list = new.columns
features = data_dummies[new_features_list]

X = features.values
Y = data_dummies['grp'].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0)
dt = c.fit(X_train, Y_train)


def dept_list(columns_list=new_features_list):
    dept_list = []
    for dept in columns_list:
        if dept.startswith('dept'):
            dept_list.append(dept)
        else:
            pass
    return dept_list


def dept_dict(ls=dept_list()):
    dept_dict = dict()
    for item in ls:
        dept_dict[item] = True
    return dept_dict


dept_dict = dept_dict()


# use to predict the group of user
def predict_group(dept='comps', dept_dict=dept_dict, is_student=True, age=19):
    department_set = dept_conversion(dept, dept_dict)
    if isinstance(is_student, bool):
        pass
    else:
        is_student = str2bool(is_student)
    group = c.predict([[is_student, age, department_set['comps'], department_set['extc']]])
    return group[0]


# Function to convert string into boolean
def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise Exception('You should enter a boolean value')


# set only one dept to true and other to false
def dept_conversion(dept, dept_dict=dept_dict):
    if dept in dept_dict:
        for key, value in dept_dict.items():
            if key == dept:
                dept_dict[key] = True
            else:
                dept_dict[key] = True
        return dept_dict
    raise Exception('The Department Doesn\'t exit')


def show_tree(tree=dt, features=new_features_list, path=r'productive_bandwidth_allocation\users\data\user_tree.png'):
    f = io.StringIO()
    export_graphviz(tree, out_file=f, feature_names=features)
    pydotplus.graph_from_dot_data(f.getvalue()).write_png(path)
    img = misc.imread(path)
    plt.rcParams["figure.figsize"] = (20, 20)
    plt.imshow(img)

# Generates a Tree
# show_tree()
