{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "777a0015-a2f9-4070-b1c1-121a739f3b48",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.preprocessing import StandardScaler, LabelEncoder\n",
    "\n",
    "# Load data\n",
    "train = pd.read_csv('D:/Yusma/project_obesity/data/processed/train.csv')\n",
    "test = pd.read_csv('D:/Yusma/project_obesity/data/processed/test.csv')\n",
    "\n",
    "# Encode categorical features\n",
    "encoder = LabelEncoder()\n",
    "for col in ['Gender', 'family_history', 'FAVC', 'CAEC', 'SMOKE', 'SCC', 'CALC', 'MTRANS']:\n",
    "    train[col] = encoder.fit_transform(train[col])\n",
    "    test[col] = encoder.transform(test[col])\n",
    "\n",
    "# Scale numerical features\n",
    "scaler = StandardScaler()\n",
    "numerical_cols = ['Age', 'Height', 'Weight', 'FCVC', 'NCP', 'CH2O', 'FAF', 'TUE']\n",
    "train[numerical_cols] = scaler.fit_transform(train[numerical_cols])\n",
    "test[numerical_cols] = scaler.transform(test[numerical_cols])\n",
    "\n",
    "# Save preprocessed data\n",
    "train.to_csv('D:/Yusma/project_obesity/data/processed/train_preprocessed.csv', index=False)\n",
    "test.to_csv('D:/Yusma/project_obesity/data/processed/test_preprocessed.csv', index=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0dd8cbe5-8acb-4bec-ba91-8b766ef1c574",
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
