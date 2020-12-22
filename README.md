autodeeplabVSothers

Al link: https://github.com/hszhao/ICNet si trova il codice degli autori di ICNet che tuttavia non forniscono il codice per l addestramento del modello. Seguendo le istruzioni nel loro repository
e possibile scaricare dei modelli pre addestrati per eseguirvi dei , tuttavia esistono altre implementazioni che raggiungono risultati migliori.


Nella cartella ICNet si puo invece trovare un implementazione piu recente di ICNet in Tensorflow : https://github.com/hellochick/ICNet-tensorflow

    pip install tensorflow-gpu==1.15 senno c e rischio inizi a girare su cpu, controllare se scrive skip gpu...

    -I pesi preaddestrati per cityscape si trovano su model e se si vogliono scaricare quelli per ADA dentro script si puo chiamare il file .py per scaricarli.
    -Per quanto riguarda i percorsi alle cartelle di dataset e gli iperparametri di train ecc si possono trovare dentro utils/config.
    -ho modificato il codice che dalla lista di immagini crea il dataset ma va rimesso originale usando come lista non la lista attuale in cityscapes ma in ICNet-tensorflow-master/data ecc
    -Nel notebook demo ci sono gli strumenti per il test sulla velocita di inferenza della rete e visualizzazione delle predizioni.

    -Gli script possono non funzionare, in caso eseguire i comandi da terminale e se ci sono errori e colpa delle versione dei vari pacchetti, settare quindi a dovere l ambiente virtuale.

    -Per la preparazione della lista di file per cityscape dentro la cartella cityscapes e presente uno script apposito
    mentre per le compatibilita dei formati occorre:
    $ export CITYSCAPES_DATASET=<cityscapes dataset path>
    $csCreateTrainIdLabelImgs
    $python -m pip install cityscapesscripts

    -Per modificare il metodo di lettura del dataset si puo modificare utils/image_reader oppure creare le liste dei file/maschere come in cityscapes/cityscapes_val_list.txt
