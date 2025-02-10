import pandas as pd

def convert_dataset(input_file, output_file):
    """
    Converts claim_similarity_dataset.tsv to the desired vclaim file format.
    Desired format: Tab-separated columns -> claim-ID, claim-text, claim-review-title, claimreview-URL, rating.
    """
    # Load the input file
    try:
        df = pd.read_csv(input_file, sep="\t", dtype=str)
    except Exception as e:
        print(f"Error reading the input file: {e}")
        return

    # Print column names for debugging
    print("Available columns:", df.columns)

    # Map the existing columns to the required columns
    column_mapping = {
        "Unnamed: 0": "claim-ID",                    # Use this column for claim-ID
        "claimReview_claimReviewed": "claim-text",  # Use this column for claim-text
        "extra_title": "claim-review-title",         # Use this column for claim-review-title
        "claimReview_url": "claim-review-url",
        "normalised_rating": "rating"               # Include the normalised_rating column as 'rating'
    }

    # Rename columns
    df.rename(columns=column_mapping, inplace=True)

    # Check for the required columns
    if not {'claim-ID', 'claim-text', 'claim-review-title','claim-review-url', 'rating'}.issubset(df.columns):
        print("The input file is missing one or more required columns: 'claim-ID', 'claim-text', 'claim-review-title','claim-review-url', 'rating'")
        return

    # Select the necessary columns and ensure they are in the correct order
    vclaim_data = df[['claim-ID', 'claim-text', 'claim-review-title','claim-review-url', 'rating']]

    # Save to the output file in the required format
    try:
        vclaim_data.to_csv(output_file, sep="\t", index=False, header=True)
        print(f"Dataset converted successfully and saved to {output_file}")
    except Exception as e:
        print(f"Error saving the output file: {e}")

if __name__ == "__main__":
    # Input and output file paths
    input_file = "claim_similarity_dataset.tsv"  # Input file
    output_file = "converted_vclaims.tsv"        # Output file

    # Convert the dataset
    convert_dataset(input_file, output_file)
