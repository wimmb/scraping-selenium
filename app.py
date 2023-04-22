from services import SocialNetworkScraper


if __name__ == '__main__':
    service = SocialNetworkScraper()

    title = "Test auto post"
    content = "Text for auto post:)"
    service.social_network_add_post(title, content)
    print('done')
