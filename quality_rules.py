def is_valid_order(order_id, customer_id):
    """Return True when both business keys are present and nonblank."""
    return (
        order_id is not None and str(order_id).strip() != ""
        and customer_id is not None and str(customer_id).strip() != ""
    )

def normalize_status(status):
    """Normalize a nullable status to lowercase trimmed text."""
    if status is None:
        return None
    return str(status).strip().lower()
