{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 50,
   "id": "compressed-fight",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "G: 5286894 \n",
      "C: 5285789\n"
     ]
    }
   ],
   "source": [
    "import zipfile\n",
    "zip_file = zipfile.ZipFile('./challenges/atgc.zip', 'r')\n",
    "zip_file.extractall('./challenges/')\n",
    "zip_file.close()\n",
    "with open('./challenges/atgc.txt', 'r') as file:\n",
    "    text = file.read()\n",
    "text = text.split('\\n')[1:]\n",
    "string_ = ''\n",
    "for i in text:\n",
    "    string_ += i\n",
    "print('G: {0} {1}C: {2}'.format(string_.count('G'), '\\n', string_.count('C')))\n",
    "file.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fallen-exploration",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
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
   "version": "3.8.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
