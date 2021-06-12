# Code Structure
* [`medmnist/`](medmnist/):
    * [`dataset.py`](medmnist/dataset.py): PyTorch datasets and dataloaders of MedMNIST.
    * [`models.py`](medmnist/models.py): *ResNet-18* and *ResNet-50* models.
    * [`breast_models.py`](medmnist/breast_models.py): Better *ResNet-18* and *ResNet-50* models for BreastMNIST.
    * [`evaluator.py`](medmnist/evaluator.py): Standardized evaluation functions.
    * [`info.py`](medmnist/info.py): Dataset information `dict` for each subset of MedMNIST.
* [`data/`](data/):
    * [`*18.txt`](data/breast18.txt): The train data for different datasets of ResNet18.
    * [`*50.txt`](data/breast50.txt): The train data for different datasets of ResNet50.
    * [`*train_loss.txt`](data/breast18_train_loss.txt): The train loss for different datasets and different Network.
    * [`*val_loss.txt`](data/breast18_val_loss.txt): The valid loss for different datasets and different Network.
* [`fig/`](fig/):
    * [`{dataname}.png`](fig/breast.png): The train curve of AUC and ACC for different datasets and different Network.
    * [`{dataname}_loss.png`](fig/breast_loss.png): The loss curve for different datasets and different Network.
* [`train.py`](train.py): The training and evaluation script to reproduce the baseline results in the paper.
* [`plot.py`](plot.py): The script to plot the needed curve.
* [`result.txt`](result.txt): The result file of our train.