NLP-Techniken im Rahmen des Projekts Data Analysis der IU

Dataset: Tripadvisor Reviews der University of Oxford (~1900 Stück).
Verwendete Techniken: Bag of Words (BoW), Term Frequency - inverse document Frequency (Tf-idf-Maß), Latente Semantische Analyse (LSA) und Latent Dirichlet Allocation (LDA).
Virtuelle Umgebung: conda
Die Dependencies sind in der Datei "environment" (yaml-Quelldatei) aufgeführt.

Die relevanten Dateien sind insbesondere LSA_BoW_Final, LSA_tf-idf_Final, LDA_BoW_Final und LDA_tf-idf_Final

Die Werte der Variablen (z. B. Anzahl der Topics und Anzahl der Top Words) wurden mehrfach getestet und schließlich wird der Code mit dem Wert 5 für die Anzahl der Topics und der Top Words als Standard zur Verfügung gestellt.
Die Werte können je nach Bedarf geänadert werden.

Falls Dateien aus dem NLTK nachgeladen werden müssen helfen folgende Zeilen:
nltk.download('punkt')
nltk.download('stopwords')
