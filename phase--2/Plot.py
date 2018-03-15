{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "[<matplotlib.lines.Line2D at 0x7f14fcce1438>]"
      ]
     },
     "execution_count": 3,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7f14fcd437b8>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "AAPL = pd.read_csv(\"AAPL.csv\") #read file csv\n",
    "\n",
    "plt.plot(AAPL['Open'],AAPL['Close']) #plot the both “open” and “close” prices.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<matplotlib.axes._subplots.AxesSubplot at 0x7f793d581860>"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<matplotlib.figure.Figure at 0x7f793d5ba6a0>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
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
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}