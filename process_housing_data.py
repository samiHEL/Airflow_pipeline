import pandas as pd
import os
from datetime import datetime

# Chemins des dossiers
to_process_dir = '/Users/sami.hella/airflow/to_process_dir'
result_dir = '/Users/sami.hella/airflow/result'
already_processed_dir = '/Users/sami.hella/airflow/already_processed'

# Fonction pour traiter un fichier CSV
def process_file(file_path):
    # Lire le fichier CSV
    df = pd.read_csv(file_path)
    
    # Calculer la moyenne des prix
    mean_price = df['price'].mean()
    
    # Créer le résultat
    result = pd.DataFrame({'mean_price': [mean_price]})
    
    # Générer le nom du fichier de résultat
    timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
    result_file = os.path.join(result_dir, f'result_{timestamp}.csv')
    
    # Sauvegarder le résultat
    result.to_csv(result_file, index=False)
    
    # Déplacer le fichier traité
    processed_file_path = os.path.join(already_processed_dir, os.path.basename(file_path))
    os.rename(file_path, processed_file_path)

# Traiter les fichiers dans le dossier toProcess
for file_name in os.listdir(to_process_dir):
    if file_name.endswith('.csv'):
        process_file(os.path.join(to_process_dir, file_name))
