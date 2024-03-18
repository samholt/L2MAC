def assign_custom_short_link(original_url, custom_short_link):
    if storage.get_original_url(custom_short_link) is not None:
        return 'Error: This short link is already in use.'
    else:
        storage.store_url(original_url, custom_short_link)
        return 'Success: Your custom short link has been assigned.'