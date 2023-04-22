from services import SocialNetworkScraper


if __name__ == '__main__':
    service = SocialNetworkScraper()

    title = "Test post"
    content = "Post content go."
    service.social_network_add_post(title, content)
    # driver = service.create_driver()
    print('done')
