{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "a39b9ba7-1705-4b9c-aae8-0731a3e2c689",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                     precision    recall  f1-score   support\n",
      "\n",
      "Insufficient_Weight       0.98      0.93      0.96        59\n",
      "      Normal_Weight       0.84      0.97      0.90        61\n",
      "     Obesity_Type_I       1.00      0.94      0.97        70\n",
      "    Obesity_Type_II       1.00      1.00      1.00        64\n",
      "   Obesity_Type_III       1.00      1.00      1.00        60\n",
      " Overweight_Level_I       0.98      0.89      0.93        55\n",
      "Overweight_Level_II       0.90      0.96      0.93        49\n",
      "\n",
      "           accuracy                           0.96       418\n",
      "          macro avg       0.96      0.96      0.96       418\n",
      "       weighted avg       0.96      0.96      0.96       418\n",
      "\n",
      "Accuracy: 0.96\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "['D:/Yusma/project_obesity/models/obesity_model.pkl']"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import pandas as pd\n",
    "from sklearn.ensemble import RandomForestClassifier\n",
    "from sklearn.metrics import classification_report, accuracy_score\n",
    "import joblib\n",
    "import os\n",
    "\n",
    "# Load preprocessed data\n",
    "train = pd.read_csv('D:/Yusma/project_obesity/data/processed/train_preprocessed.csv')\n",
    "test = pd.read_csv('D:/Yusma/project_obesity/data/processed/test_preprocessed.csv')\n",
    "\n",
    "# Pisahkan fitur dan target\n",
    "X_train = train.drop(columns=['Obesity'])\n",
    "y_train = train['Obesity']\n",
    "X_test = test.drop(columns=['Obesity'])\n",
    "y_test = test['Obesity']\n",
    "\n",
    "# Latih model\n",
    "model = RandomForestClassifier(random_state=42)\n",
    "model.fit(X_train, y_train)\n",
    "\n",
    "# Evaluasi model\n",
    "y_pred = model.predict(X_test)\n",
    "print(classification_report(y_test, y_pred))\n",
    "print(f\"Accuracy: {accuracy_score(y_test, y_pred):.2f}\")\n",
    "\n",
    "# Simpan model\n",
    "os.makedirs('D:/Yusma/project_obesity/models', exist_ok=True)\n",
    "joblib.dump(model, 'D:/Yusma/project_obesity/models/obesity_model.pkl')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "15b6dc1a-a059-4ac0-a200-c50ba94a7a46",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.2"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
