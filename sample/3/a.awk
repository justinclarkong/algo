#!/usr/bin/awk -f
function bomb(a, b, t) {
	return (V[a] > V[b] ? (V[a] <= V[t] || V[t] <= V[b]) : (V[a] <= V[t] && V[t] <= V[b]))
}

NR > 1 {
	for (i = 1; i <= NF; ++i)
		V[++ptr] = $i
}

END {
	for (i = 1; i < ptr; i += 2) {
		k = 0

		for (j = 1; j < ptr; j += 4)
			if (bomb(j, j+1, i) || bomb(j, j+1, i+1))
				k += 1
			else
				a[j+2] = 1

		for (_i in a) {
			_k = 0

			for (j in a)
				if (bomb(j, j+1, _i) || bomb(j, j+1, _i + 1))
					_k += 1

			if (_k > _max)
				_max = _k
		}

		if (k + _max > max)
			max = k + _max

		split("", a)
		_max = 0
	}

	print(max)
}
