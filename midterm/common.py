config = {
  'drop_columns': ['neo_reference_id', 'name', 'close_approach_date', 'epoch_date_close_approach', 'orbit_determination_date', 'orbit_id', 'equinox', 'orbiting_body'],
  'missing_values': ['n/a', 'na', '--', '-', '?'],
  'replacements': {' ':'_', '(':'_',')':'','.':'' },
  'seed': 666,
  'vectorizer_file_name': 'vectorizer.out',
  'model_file_name': 'model.out'
}