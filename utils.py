def filter_as400_applications(applications):
    """
    Filter applications to include only those with quality_model "AS400"
    """
    return [app for app in applications if app.get('quality_model') == 'AS400']
