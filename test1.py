def process_user(user):
    if user.is_active():
        # +1 (if)
        if user.has_profile():
            # +1 (if) +1 (nested)
            # ... process active user with profile
        else:
            # +1 (else)
            # ... process active user without profile
    else:
        # +1 (else)
        if user.has_profile():
            # +1 (if) +1 (nested)
            # ... process inactive user with profile
        else:
            # +1 (else)
            # ... process inactive user without profile

# Example usage:
some_user = User("Alice", active=True, has_profile=True)
process_user(some_user)
