from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, cap: int):
        self.cap = cap
        self.key_to_val = {}  # key -> value
        self.key_to_freq = {}  # key -> freq
        self.freq_to_keys = defaultdict(OrderedDict)  # freq -> OrderedDict of keys
        self.min_freq = 0

    def _update_freq(self, key: int):
        freq = self.key_to_freq[key]
        val = self.key_to_val[key]
        
        # Remove the key from the current frequency list
        del self.freq_to_keys[freq][key]
        if not self.freq_to_keys[freq]:
            del self.freq_to_keys[freq]
            if self.min_freq == freq:
                self.min_freq += 1
        
        # Add to higher frequency
        self.key_to_freq[key] = freq + 1
        self.freq_to_keys[freq + 1][key] = val

    def get(self, key: int) -> int:
        if key not in self.key_to_val:
            return -1
        
        self._update_freq(key)
        return self.key_to_val[key]

    def put(self, key: int, value: int) -> None:
        if self.cap == 0:
            return

        if key in self.key_to_val:
            self.key_to_val[key] = value
            self._update_freq(key)
            return

        if len(self.key_to_val) >= self.cap:
            # Evict LFU -> LRU from freq_to_keys[min_freq]
            key_to_evict, _ = self.freq_to_keys[self.min_freq].popitem(last=False)
            del self.key_to_val[key_to_evict]
            del self.key_to_freq[key_to_evict]
            if not self.freq_to_keys[self.min_freq]:
                del self.freq_to_keys[self.min_freq]

        # Insert new key
        self.key_to_val[key] = value
        self.key_to_freq[key] = 1
        self.freq_to_keys[1][key] = value
        self.min_freq = 1