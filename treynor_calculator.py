def calculate_treynor_ratio(return_=None, beta=None, risk_free_rate=None, treynor_ratio=None):
    """
    Calculate the Treynor Ratio or any missing value (Return, Beta, Risk-Free Rate) given the other three.

    Parameters:
        return_ (float): Portfolio return (as a decimal or percentage).
        beta (float): Portfolio beta.
        risk_free_rate (float): Risk-free rate (as a decimal or percentage).
        treynor_ratio (float): Treynor Ratio.

    Returns:
        dict: Contains the calculated value and the other inputs.
    """
    # Ensure at least three values are provided
    inputs = [return_, beta, risk_free_rate, treynor_ratio]
    if inputs.count(None) > 1:
        return "Error: Provide at least three values to calculate the missing one."

    # Calculate Treynor Ratio if missing
    if treynor_ratio is None:
        if return_ is not None and beta is not None and risk_free_rate is not None:
            treynor_ratio = (return_ - risk_free_rate) / beta
        else:
            return "Error: Insufficient data to calculate Treynor Ratio."

    # Calculate Return if missing
    elif return_ is None:
        if treynor_ratio is not None and beta is not None and risk_free_rate is not None:
            return_ = treynor_ratio * beta + risk_free_rate
        else:
            return "Error: Insufficient data to calculate Return."

    # Calculate Beta if missing
    elif beta is None:
        if treynor_ratio is not None and return_ is not None and risk_free_rate is not None:
            beta = (return_ - risk_free_rate) / treynor_ratio
        else:
            return "Error: Insufficient data to calculate Beta."

    # Calculate Risk-Free Rate if missing
    elif risk_free_rate is None:
        if treynor_ratio is not None and beta is not None and return_ is not None:
            risk_free_rate = return_ - (treynor_ratio * beta)
        else:
            return "Error: Insufficient data to calculate Risk-Free Rate."

    # Return all values
    return {
        "Return": return_,
        "Beta": beta,
        "Risk-Free Rate": risk_free_rate,
        "Treynor Ratio": treynor_ratio,
    }

# Example Usage with User Input
if __name__ == "__main__":
    print("Enter the values for the following. Type 'None' for the missing value:")
    try:
        return_ = input("Return (as decimal, e.g., 0.15 for 15%): ")
        beta = input("Beta: ")
        risk_free_rate = input("Risk-Free Rate (as decimal, e.g., 0.03 for 3%): ")
        treynor_ratio = input("Treynor Ratio: ")

        # Convert inputs to floats or None
        return_ = float(return_) if return_.lower() != "none" else None
        beta = float(beta) if beta.lower() != "none" else None
        risk_free_rate = float(risk_free_rate) if risk_free_rate.lower() != "none" else None
        treynor_ratio = float(treynor_ratio) if treynor_ratio.lower() != "none" else None

        # Calculate and print result
        result = calculate_treynor_ratio(return_, beta, risk_free_rate, treynor_ratio)
        print("Calculated Values:", result)
    except ValueError:
        print("Invalid input. Please enter numeric values or 'None' for missing values.")
