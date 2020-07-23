def model_eval(model):
    """Quickly fit, predict, and evaluate model using classification report, confusion matrices, and 
    train/test accuracy scores"""
    model.fit(X_train_tsvd, y_train)
    y_test_preds = model.predict(X_test_tsvd)
    y_train_preds = model.predict(X_train_tsvd)
    print(classification_report(y_test, y_test_preds))
    print(confusion_matrix(y_test, y_test_preds))
    print("Training Accuracy Score -> ",accuracy_score(y_train, y_train_preds)*100)
    print("Test Accuracy Score -> ",accuracy_score(y_test, y_test_preds)*100)
