def calculate_energy(capacity_ah, voltage, level_percent):
    """Calcule l'énergie disponible en Wh."""
    return capacity_ah * voltage * (level_percent / 100)

def estimate_autonomy(available_wh, consumption_w):
    """Estime l'autonomie en heures."""
    if consumption_w == 0:
        return 0
    return available_wh / consumption_w

def get_recommendations(level_percent, appliances):
    """
    Algorithme de conseil SolarGuard. 
    Analyse le niveau de batterie et classifie les appareils.
    """
    recommended = []
    acceptable = []
    avoid = []
    
    # Détermination de l'état du système
    if level_percent > 70:
        status = "OPTIMAL"
        message = "Batterie bien chargée. Vous pouvez utiliser vos appareils de confort."
        icon = "ph-check-circle"
        color = "var(--success)"
    elif level_percent > 30:
        status = "VIGILANCE"
        message = "Niveau moyen. Privilégiez les appareils essentiels."
        icon = "ph-warning-circle"
        color = "var(--warning)"
    else:
        status = "CRITIQUE"
        message = "Batterie faible ! Coupez tout le superflu pour préserver l'éclairage."
        icon = "ph-prohibit"
        color = "var(--danger)"
    
    for app in appliances:
        # Logique de classification intelligente
        if status == "OPTIMAL":
            if app.power_w < 500: recommended.append(app)
            else: acceptable.append(app)
        
        elif status == "VIGILANCE":
            if app.is_essential: recommended.append(app)
            elif app.power_w < 100: acceptable.append(app)
            else: avoid.append(app)
            
        else: # CRITIQUE
            if app.is_essential and app.power_w < 50: recommended.append(app)
            elif app.is_essential: acceptable.append(app)
            else: avoid.append(app)
                
    return {
        'status': status,
        'message': message,
        'icon': icon,
        'color': color,
        'recommended': recommended,
        'acceptable': acceptable,
        'avoid': avoid
    }

def get_usage_history(user):
    # Get last 7 readings
    from .models import BatteryReading
    import json
    
    readings = BatteryReading.objects.filter(user=user).order_by('-timestamp')[:7]
    readings = reversed(readings) # Chronological order
    
    labels = []
    data = []
    
    for r in readings:
        labels.append(r.timestamp.strftime("%d/%m %H:%M"))
        data.append(r.level_percent)
        
    return json.dumps({
        'labels': labels,
        'data': data
    })
