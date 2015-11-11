from mltsp import build_model
from mltsp import cfg
from nose.tools import with_setup
import numpy.testing as npt
import os
from os.path import join as pjoin
from sklearn.externals import joblib
import shutil


DATA_PATH = pjoin(os.path.dirname(__file__), "data")


def copy_classification_test_data():
    fnames = ["test_featureset.nc"]
    for fname in fnames:
        shutil.copy(pjoin(DATA_PATH, fname), cfg.FEATURES_FOLDER)


def copy_regression_test_data():
    fnames = ["test_reg_featureset.nc"]
    for fname in fnames:
        shutil.copy(pjoin(DATA_PATH, fname), cfg.FEATURES_FOLDER)


def remove_test_data():
    fnames = ["test_featureset.nc", "test_reg_featureset.nc", "test.pkl"]
    for fname in fnames:
        for data_dir in [cfg.FEATURES_FOLDER, cfg.MODELS_FOLDER]:
            try:
                os.remove(pjoin(data_dir, fname))
            except OSError:
                pass


@with_setup(copy_classification_test_data, remove_test_data)
def test_build_model_rfc():
    """Test main model building method - RFC"""
    build_model.create_and_pickle_model("test", "RFC", "test")
    model = joblib.load(pjoin(cfg.MODELS_FOLDER, "test.pkl"))
    assert hasattr(model, "predict_proba")
    assert "sklearn.ensemble.forest.RandomForestClassifier" in str(type(model))


@with_setup(copy_regression_test_data, remove_test_data)
def test_build_model_rfr():
    """Test main model building method - RFR"""
    build_model.create_and_pickle_model("test", "RFR", "test_reg")
    model = joblib.load(pjoin(cfg.MODELS_FOLDER, "test.pkl"))
    assert hasattr(model, "predict")
    assert "sklearn.ensemble.forest.RandomForestRegressor" in str(type(model))


@with_setup(copy_classification_test_data, remove_test_data)
def test_build_model_lin_class():
    """Test main model building method - linear classifier"""
    build_model.create_and_pickle_model("test", "LC", "test")
    model = joblib.load(pjoin(cfg.MODELS_FOLDER, "test.pkl"))
    assert hasattr(model, "predict")
    assert "SGDClassifier" in str(type(model))


@with_setup(copy_regression_test_data, remove_test_data)
def test_build_model_lin_reg():
    """Test main model building method - linear regressor"""
    build_model.create_and_pickle_model("test", "LR", "test_reg")
    model = joblib.load(pjoin(cfg.MODELS_FOLDER, "test.pkl"))
    assert hasattr(model, "predict")
    assert "LinearRegression" in str(type(model))


@with_setup(copy_classification_test_data, remove_test_data)
def test_build_model_ridge_cv():
    """Test main model building method - Ridge Classifer CV"""
    build_model.create_and_pickle_model("test", "RC", "test")
    model = joblib.load(pjoin(cfg.MODELS_FOLDER, "test.pkl"))
    assert hasattr(model, "predict")
    assert "RidgeClassifierCV" in str(type(model))


@with_setup(copy_regression_test_data, remove_test_data)
def test_build_model_ard_reg():
    """Test main model building method - ARD Regression"""
    build_model.create_and_pickle_model("test", "ARDR", "test_reg")
    model = joblib.load(pjoin(cfg.MODELS_FOLDER, "test.pkl"))
    assert hasattr(model, "predict")
    assert "ARDRegression" in str(type(model))
