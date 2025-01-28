NLP-Techniken im Rahmen des Projekts Data Analysis der IU

Virtuelle Umgebung: conda
Die Dependencies sind in der Datei "environment" (yaml-Quelldatei) aufgeführt.

Die relevanten Dateien sind insbesondere LSA_BoW_Final, LSA_tf-idf_Final, LDA_BoW_Final und LDA_tf-idf_Final

Die Werte (z. B. Anzahl der Topics und Anzahl der Top Words) wurden mehrfach getestet und schließlich wird der Code mit dem Wert 5 für die Anzahl der Topics und der Top Words als Standard zur Verfügung gestellt.

Falls Dateien aus dem NLTK nachgeladen werden müssen helfen folgende Zeilen:
nltk.download('punkt')
nltk.download('stopwords')
