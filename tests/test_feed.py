from crisis import Feed


def test_soufriere():
    feed = Feed.from_rss_url("https://rss.app/feeds/wTXzZFTDgpaDTNTc.xml")
    assert len(feed.tweets[0].description) > 0
