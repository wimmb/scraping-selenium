from services import SocialNetworkScraper


if __name__ == '__main__':
    service = SocialNetworkScraper()
    service.social_network_login()
    # driver = service.create_driver()
    print('done')
