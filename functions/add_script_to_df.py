def add_script_to_df(index, script, df):
    """add script to df at specified index"""
    df.at[index,'script'] = script
