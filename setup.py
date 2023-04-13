#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys
import os

try:
    sys.path.index(os.getcwd()) # os.getcwd() for this directory
except ValueError:
    sys.path.append(os.getcwd())

import pandas as pd
from pandas.plotting import scatter_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from utils import analysis_utils

from sklearn.model_selection import (
    train_test_split,
    cross_val_score,
    cross_val_predict, 
    GridSearchCV
)
from sklearn.metrics import (
    accuracy_score,
    roc_curve,
    roc_auc_score,
    confusion_matrix,
    precision_score, 
    recall_score,
    precision_recall_curve,
    f1_score,
)
from sklearn.neural_network import MLPClassifier
