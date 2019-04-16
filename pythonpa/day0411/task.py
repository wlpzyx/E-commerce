from pybloom_live import ScalableBloomFilter


sdf = ScalableBloomFilter(initial_capacity=100, error_rate=0.001,
                          mode=ScalableBloomFilter.LARGE_SET_GROWTH)