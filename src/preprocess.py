{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "aae7f7f9-73ed-4c65-8371-e984ef4df339",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "from sklearn.model_selection import train_test_split\n",
    "\n",
    "# Load dataset\n",
    "data = pd.read_csv('D:/Yusma/project_obesity/data/raw/obesity_prediction.csv')\n",
    "\n",
    "# Hapus duplikat\n",
    "data = data.drop_duplicates()\n",
    "\n",
    "# Splitting data\n",
    "train, test = train_test_split(data, test_size=0.2, random_state=42)\n",
    "\n",
    "# Simpan data hasil splitting\n",
    "train.to_csv('D:/Yusma/project_obesity/data/processed/train.csv', index=False)\n",
    "test.to_csv('D:/Yusma/project_obesity/data/processed/test.csv', index=False)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "696ffd50-91bf-4926-8dd1-e5c90d168ff1",
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
