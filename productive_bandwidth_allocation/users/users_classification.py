import io

import pandas as pd  # DataFrame, Series
import pydotplus
from matplotlib import pyplot as plt
from scipy import misc
# from IPython.display import display # for displaying the data
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import export_graphviz

DATA_PATH = r'productive_bandwidth_allocation\users\data'
# Reading the data
data = pd.read_csv(DATA_PATH + r'\users.csv', header=None, index_col=False,
                   names=['department',
                          'is_student',
                          'age',
                          'group'])

# It is used for One-Hot encoding
data_dummies = pd.get_dummies(data)

# ID3 Decision Tree algorithm has been used criterion="entropy"
c = DecisionTreeClassifier(criterion="entropy")

# selecting all the columns for features except group which is a label
new = data_dummies.ix[:]
new.pop('group')
new_features_list = new.columns
features = data_dummies[new_features_list]

X = features.values
Y = data_dummies['group'].values

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, random_state=0)
dt = c.fit(X_train, Y_train)

plain_dept_list = []


def department_list(columns_list=new_features_list):
    department_list = []
    for department in columns_list:
        if department.startswith('department'):
            department_list.append(department)
            plain_dept_list.append(department.replace('department_', '').upper())
        else:
            pass
    return department_list


department_list = department_list()


def department_dict(depatment_list=department_list):
    department_dict = dict()
    for item in depatment_list:
        department_dict[item] = True
    return department_dict


department_dict = department_dict()


def department_exist(department_name, department_list=plain_dept_list):
    for departments in department_list:
        if departments.lower() == department_name.lower():
            return True
    raise Exception(f"{department_name} Department Doesn't exist")


# set only one department to true and other to false
def department_conversion(department_name, department_dict=department_dict):
    if department_exist(department_name):
        for key, value in department_dict.items():
            strip_key = key.replace('department_', '')
            if strip_key.lower() == department_name.lower():
                department_dict[key] = True
            else:
                department_dict[key] = False
        return department_dict


# use to predict the group of user
def predict_group(department_name='Computer', department_dict=department_dict, is_student=True, age=19):
    department_set = department_conversion(department_name, department_dict)
    if isinstance(is_student, bool):
        pass
    else:
        is_student = str2bool(is_student)
    group = c.predict([[is_student, age] + list(department_set.values())])
    return group[0]


# Function to convert string into boolean
def str2bool(v):
    if v.lower() in ('yes', 'true', 't', 'y', '1'):
        return True
    elif v.lower() in ('no', 'false', 'f', 'n', '0'):
        return False
    else:
        raise Exception('You should enter a boolean value')


def show_tree(tree=dt, features=new_features_list, path=DATA_PATH + r'\user_tree.png'):
    f = io.StringIO()
    export_graphviz(tree, out_file=f, feature_names=features)
    pydotplus.graph_from_dot_data(f.getvalue()).write_png(path)
    img = misc.imread(path)
    plt.rcParams["figure.figsize"] = (20, 20)
    plt.imshow(img)

# Generates a Tree
# show_tree()
