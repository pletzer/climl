process aggregate {
    input:
    path scores

    output:
    path 'lonlatseed.csv'

    script:
    """
    aggregate.py ${scores}
    """
}