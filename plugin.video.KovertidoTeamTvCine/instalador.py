# Python code obfuscated by www.development-tools.net 
 

import base64, codecs
magic = 'aW1wb3J0IHVzZXJ2YXINCmltcG9ydCB4Ym1jLCB4Ym1jZ3VpLCB1cmxsaWIsIHN5cywgdGltZSwgdXNlcnZhciwgb3MNCmltcG9ydCB3aXphcmQgYXMgd2l6DQppbXBvcnQgZG93bmxvYWRlcixleHRyYWN0DQoNCkNPTE9SMSAgICAgICAgID0gdXNlcnZhci5DT0xPUjENCkNPTE9SMiAgICAgICAgID0gdXNlcnZhci5DT0xPUjINCg0KI3VybGxpYi5VUkxvcGVuZXIudmVyc2lvbiA9ICdNb3ppbGxhLzUuMCAoV2luZG93cyBOVCA2LjEpIEFwcGxlV2ViS2l0LzUzNy4zNiAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8zNS4wLjE5MTYuMTUzIFNhZmFyaS81MzcuMzYgU0UgMi5YIE1ldGFTciAxLjAnDQoNCmltcG9ydCB4Ym1jZ3VpDQojIGltcG9ydCB1cmxsaWIyDQppbXBvcnQgc29ja2V0DQppbXBvcnQga29kaQ0KaW1wb3J0IHRpbWUNCkFERE9OX0lEICAgICAgICAgPSB1c2VydmFyLkFERE9OX0lEDQpBRERPTlRJVExFICAgICAgID0gdXNlcnZhci5BRERPTlRJVExFDQpBRERPTiAgICAgICAgICAgID0gd2l6LmFkZG9uSWQoQURET05fSUQpDQpWRVJTSU9OICAgICAgICAgID0gd2l6LmFkZG9uSW5mbyhBRERPTl9JRCwndmVyc2lvbicpDQpBRERPTlBBVEggICAgICAgID0gd2l6LmFkZG9uSW5mbyhBRERPTl9JRCwgJ3BhdGgnKQ0KRElBTE9HICAgICAgICAgICA9IHhibWNndWkuRGlhbG9nKCkNCkRQICAgICAgICAgICAgICAgPSB4Ym1jZ3VpLkRpYWxvZ1Byb2dyZXNzKCkNCkhPTUUgICAgICAgICAgICAgPSB4Ym1jLnRyYW5zbGF0ZVBhdGgoJ3NwZWNpYWw6Ly9ob21lLycpDQpMT0cgICAgICAgICAgICAgID0geGJtYy50cmFuc2xhdGVQYXRoKCdzcGVjaWFsOi8vbG9ncGF0aC8nKQ0KUFJPRklMRSAgICAgICAgICA9IHhibWMudHJhbnNsYXRlUGF0aCgnc3BlY2lhbDovL3Byb2ZpbGUvJykNClRFTVBESVIgICAgICAgICAgPSB4Ym1jLnRyYW5zbGF0ZVBhdGgoJ3NwZWNpYWw6Ly90ZW1wJykNCkFERE9OUyAgICAgICAgICAgPSBvcy5wYXRoLmpvaW4oSE9NRSwgICAgICAnYWRkb25zJykNClVTRVJEQVRBICAgICAgICAgPSBvcy5wYXRoLmpvaW4oSE9NRSwgICAgICAndXNlcmRhdGEnKQ0KUExVR0lOICAgICAgICAgICA9IG9zLnBhdGguam9pbihBRERPTlMsICAgIEFERE9OX0lEKQ0KUEFDS0FHRVMgICAgICAgICA9IG9zLnBhdGguam9pbihBRERPTlMsICAgICdwYWNrYWdlcycpDQpBRERPTkQgICAgICAgICAgID0gb3MucGF0aC5qb2luKFVTRVJEQVRBLCAgJ2FkZG9uX2RhdGEnKQ0KQURET05EQVRBICAgICAgICA9IG9zLnBhdGguam9pbihVU0VSREFUQSwgICdhZGRvbl9kYXRhJywgQURET05fSUQpDQpBRFZBTkNFRCAgICAgICAgID0gb3MucGF0aC5qb2luKFVTRVJEQVRBLCAgJ2FkdmFuY2Vkc2V0dGluZ3MueG1sJykNClNPVVJDRVMgICAgICAgICAgPSBvcy5wYXRoLmpvaW4oVVNFUkRBVEEsICAnc291cmNlcy54bWwnKQ0KRkFWT1VSSVRFUyAgICAgICA9IG9zLnBhdGguam9pbihVU0VSREFUQSwgICdmYXZvdXJpdGVzLnhtbCcpDQpQUk9GSUxFUyAgICAgICAgID0gb3MucGF0aC5qb2luKFVTRVJEQVRBLCAgJ3Byb2ZpbGVzLnhtbCcpDQpHVUlTRVRUSU5HUyAgICAgID0gb3MucGF0aC5qb2luKFVTRVJEQVRBLCAgJ2d1aXNldHRpbmdzLnhtbCcpDQpUSFVNQlMgICAgICAgICAgID0gb3MucGF0aC5qb2luKFVTRVJEQVRBLCAgJ1RodW1ibmFpbHMnKQ0KREFUQUJBU0UgICAgICAgICA9IG9zLnBhdGguam9pbihVU0VSREFUQSwgICdEYXRhYmFzZScpDQpNWVZJREVPUwkgICAgID0gb3MucGF0aC5qb2luKERBVEFCQVNFLCAgJ015VmlkZW9zMTE2LmRiJykNCkZBTkFSVCAgICAgICAgICAgPSBvcy5wYXRoLmpvaW4oUExVR0lOLCAgICAnZmFuYXJ0LmpwZycpDQpJQ09OICAgICAgICAgICAgID0gb3MucGF0aC5qb2luKFBMVUdJTiwgICAgJ2ljb24ucG5nJykNCkFSVCAgICAgICAgICAgICAgPSBvcy5wYXRoLmpvaW4oUExVR0lOLCAgICAncmVzb3VyY2VzJywgJ2FydCcpDQpXSVpMT0cgICAgICAgICAgID0gb3MucGF0aC5qb2luKEFERE9OREFUQSwgJ3dpemFyZC5sb2cnKQ0KU1BFRURURVNURk9MRCAgICA9IG9zLnBhdGguam9pbihBRERPTkRBVEEsICdTcGVlZFRlc3QnKQ0KQVJDSElWRV9DQUNIRSAgICA9IG9zLnBhdGguam9pbihURU1QRElSLCAgICdhcmNoaXZlX2NhY2hlJykNClNLSU4gICAgICAgICAgICAgPSB4Ym1jLmdldFNraW5EaXIoKQ0KS09ESVYgICAgICAgICAgICA9IGZsb2F0KHhibWMuZ2V0SW5mb0xhYmVsKCJTeXN0ZW0uQnVpbGRWZXJzaW9uIilbOjRdKQ0KI2lmIEtPRElWID4gMTc6DQoJI2ltcG9ydCB6ZmlsZSBhcyB6aXBmaWxlDQojZWxzZToNCmltcG9ydCB6aXBmaWxlDQoNCmRlZiBwYWNrSW5zdGFsbGVyKG5hbWUsIHVybCk6DQogICAgaW1wb3J0IHhibWN2ZnMNCiAgICAjaWYgbm90IHdpei53b3JraW5nVVJMKHVybCkgPT0gVHJ1ZTogd2l6LkxvZ05vdGlmeSgiW0NPTE9SICVzXUluc3RhbGFkb3IgZGUgQWRkb25zWy9DT0xPUl0iICUgQ09MT1IxLCAnW0NPTE9SICVzXSVzOlsvQ09MT1JdIFtDT0xPUiAlc11aaXAgVXJsIEludmFsaWRhWy9DT0xPUl0nICUgKENPTE9SMSwgbmFtZSwgQ09MT1IyKSk7IHJldHVybg0KICAgIGlmIG5vdCBvcy5wYXRoLmV4aXN0cyhQQUNLQUdFUyk6IG9zLm1ha2VkaXJzKFBBQ0tBR0VTKQ0KICAgIERQLmNyZWF0ZShBRERPTlRJVExFLCdbQ09MT1IgJXNdRGVzY2FyZ2FuZG86Wy9DT0xPUl0gW0NPTE9SICVzXSVzWy9DT0xPUl0nICUgKENPTE9SMiwgQ09MT1IxLCBuYW1lKSkNCiAgICB1cmxzcGxpdHMgPSB1cmwuc3BsaXQoJy8nKQ0KICAgIGxpYiA9IHhibWN2ZnMubWFrZUxlZ2FsRmlsZW5hbWUob3MucGF0aC5qb2luKFBBQ0tBR0VTLCB1cmxzcGxpdHNbLTFdKSkNCiAgICB0cnk6IG9zLnJlbW92ZShsaWIpDQogICAgZXhjZXB0OiBwYXNzDQogICAgZG93bmxvYWRlci5kb3dubG9hZCh1cmwsIGxpYiwgRFApDQogICAgdGl0bGUgPSAnW0NPTE9SICVzXUluc3RhbGFuZG86Wy9DT0xPUl0gW0NPTE9SICVzXSVzWy9DT0xPUl0nICUgKENPTE9SMiwgQ09MT1IxLCBuYW1lKQ0KICAgIERQLnVwZGF0ZSgwLCAnW0NPTE9SICVzXUVzcGVyYVsvQ09MT1JdJyAlIENPTE9SMikNCiAgICBleHRyYWN0LmFsbChsaWIsQURET05TLERQKQ0KICAgIGluc3RhbGxlZCA9IGdyYWJBZGRvbnMobGliKQ0KICAgIHdpei5hZGRvbkRhdGFiYXNlKGluc3RhbGxlZCwgMSwgVHJ1ZSkNCiAgICBEUC5jbG9zZSgpDQogICAgd2l6LkxvZ05vdGlmeSgiW0NPTE9SICVzXUluc3RhbGFkb3IgZGUgQWRkb25zWy9DT0xPUl0iICUgQ09MT1IxLCAnW0NPTE9SICVzXSVzOiBJbnN0YWxhZG8hWy9DT0xPUl0nICUgKENPTE9SMiwgbmFtZSkpDQogICAgd2l6LmViaSgnVXBkYXRlQWRkb25SZXBvcygpJykNCiAgICB3aXouZWJpKCdVcGRhdGVMb2NhbEFkZG9ucygpJykNCiAgICB3aXoucmVmcmVzaCgpDQoNCg0KZGVmIGFkZG9uSW5zdGFsbGVyKHBsdWdpbiwgdXJsKToNCiAgICBpbXBvcnQgdXNlcnZhcg0KICAgIGltcG9ydCB4Ym1jLCB4Ym1jZ3VpLCB1cmxsaWIsIHN5cywgdGltZSwgdXNlcnZhciwgb3MNCiAgICBpbXBvcnQgd2l6YXJkIGFzIHdpeg0KICAgIGltcG9ydCBkb3dubG9hZGVyLGV4dHJhY3QNCiAgICB1cmwgPSBOb25lDQogICAgI3VybD0naHR0cDovL3BlcmlsbGFzLm1lbmRlbHV4LmVzL3BsdWdpbi52aWRlby5zdHViZXZhdm9vMi56aXAnDQogICAgQURET05GSUxFICAgICAgPSAnaHR0cDovL3BlcmlsbGFzLm1lbmRlbHV4LmVzL2FkZG9ucy50eHQnDQogICAgaWYgICdodHRwOi8vJyBpbiBBRERPTkZJTEUgOg0KICAgICNpZiAgbm90IEFERE9ORklMRSA9PSAnaHR0cDovLyc6DQogICAgICAgIGlmIHVybCA9PSBOb25lOiB1cmwgPSBBRERPTkZJTEUNCiAgICAgICAgQURET05XT1JLSU5HID0gd2l6LndvcmtpbmdVUkwodXJsKQ0KICAgICAgICBpZiBBRERPTldPUktJTkcgPT0gVHJ1ZToNCiAgICAgICAgICAgIGxpbmsgPSB3aXoudGV4dENhY2hlKHVybCkucmVwbGFjZSgnXG4nLCcnKS5yZXBsYWNlKCdccicsJycpLnJlcGxhY2UoJ1x0JywnJykucmVwbGFjZSgncmVwb3NpdG9yeT0iIicsICdyZXBvc2l0b3J5PSJub25lIicpLnJlcGxhY2UoJ3JlcG9zaXRvcnl1cmw9IiInLCAncmVwb3NpdG9yeXVybD0iaHR0cDovLyInKS5yZXBsYWNlKCdyZXBvc2l0b3J5eG1sPSIiJywgJ3JlcG9zaXRvcnl4bWw9Imh0dHA6Ly8iJykNCiAgICAgICAgICAgIG1hdGNoID0gcmUuY29tcGlsZSgnbmFtZT0iKC4rPykiLis/bHVnaW49IiVzIi4rP3JsPSIoLis/KSIuKz9lcG9zaXRvcnk9IiguKz8pIi4rP2Vwb3NpdG9yeXhtbD0iKC4rPykiLis/ZXBvc2l0b3J5dXJsPSIoLis/KSIuKz9jb249IiguKz8pIi4rP2FuYXJ0PSIoLis/KSIuKz9kdWx0PSIoLis/KSIuKz9lc2NyaXB0aW9uPSIoLis/KSInICUgcGx1Z2luKS5maW5kYWxsKGxpbmspDQogICAgICAgICAgICBpZiBsZW4obWF0Y2gpID4gMDoNCiAgICAgICAgICAgICAgICBmb3IgbmFtZSwgdXJsLCByZXBvc2l0b3J5LCByZXBvc2l0b3J5eG1sLCByZXBvc2l0b3J5dXJsLCBpY29uLCBmYW5hcnQsIGFkdWx0LCBkZXNjcmlwdGlvbiBpbiBtYXRjaDoNCiAgICAgICAgICAgICAgICAgICAgaWYgb3M'
love = 'hpTS0nP5yrTymqUZbo3ZhpTS0nP5do2yhXRSRER9BHljtpTk1M2yhXFx6QDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOxolNtVPNtVPNtCFOoW1gQG0kCHvOfnJ1yKIgPKHSvpzylVRSxMT9hJl9PKIfiD09ZG1WqWljtW1gQG0kCHvOlMJEqJ0WqDz9lpzSlVRSxMT9hJl9PKIfiD09ZG1WqW10APvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUAyoTIwqTIxVQ0tERyOGR9UYaAyoTIwqPtvJ0ACGR9FVPImKIgQG0kCHvO5MJkfo3qqJ0WqDJExo24trJRtnJ5mqTSfLJEiYPOkqJHtpKIcMKWyplObLJAypw9oY0WqJl9QG0kCHy0vVPHtD09ZG1VlYPOxolxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTyzVUAyoTIwqTIxVQ09VQN6QDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtq2y6YzIvnFtaHaIhDJExo24bWKZcWlNyVUOfqJqcovxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPO4Lz1wYaAfMJIjXQHjZPxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOlMKE1pz4tIUW1MD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtMJkcMvOmMJkyL3EyMPN9CFNkBt0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUqcrv5woTIuoxuiqKAyXT9mYaOuqTthnz9covuOERECGyZfVUOfqJqcovxcQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtqUW5BvO3nKbhpzIgo3MyEz9fMTIlXT9mYaOuqTthnz9covuOERECGyZfVUOfqJqcovxcQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtMKuwMKO0BvOjLKAmQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtnJLtERyOGR9UYayyp25iXRSRER9BIRyHGRHfVPWoD09ZG1VtWKAqHKIcMKWyplOvo3WlLKVtoTRtL2SlpTI0LFOuMTEioy9xLKEuVTEyBvVtWFOQG0kCHwVfVPWoD09ZG1VtWKAqWKAoY0ACGR9FKG9oY0ACGR9FKFVtWFNbD09ZG1VkYPOjoUIanJ4cYPO5MKAfLJWyoQ0vJ0ACGR9FVUAjpzyhM2qlMJIhKHWipaWupyfiD09ZG1WqVvjtoz9fLJWyoQ0vJ0ACGR9FVUWyMS1GLJk0LKWoY0ACGR9FKFVcBt0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOlMJ1iqzIOMTEioxEuqTRbpTk1M2yhXD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUqcrv5lMJMlMKAbXPxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOlMKE1pz4tIUW1MD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtMJkmMGbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOlMKE1pz4tEzSfp2HAPvNtVPNtVPNtVPNtVPNtVPNtVPNtpzIjolN9VT9mYaOuqTthnz9covuOERECGyZfVUWypT9mnKEipaxcQDbtVPNtVPNtVPNtVPNtVPNtVPNtVTyzVT5iqPOlMKOip2y0o3W5Yzkiq2IlXPxtCG0tW25iozHaVTShMPOho3Dto3ZhpTS0nP5yrTymqUZbpzIjolx6QDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPO3nKbhoT9aXPWFMKOip2y0o3W5VT5iqPOcoaA0LJkfMJDfVTyhp3EuoTkcozptnKDvXD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtnJLtERyOGR9UYayyp25iXRSRER9BIRyHGRHfVPWoD09ZG1VtWKAqI291oTDtrJ91VTkcn2HtqT8tnJ5mqTSfoPO0nTHtpzIjo3AcqT9lrFOzo3VtJ0ACGR9FVPImKFImJl9QG0kCHy06VvNyVPuQG0kCHwVfVRACGR9FZFjtpTk1M2yhXFjtVygQG0kCHvNyp10yp1fiD09ZG1WqC1fiD09ZG1WqVvNyVPuQG0kCHwRfVUWypT9mnKEipaxcYPO5MKAfLJWyoQ0vJ0ACGR9FVUAjpzyhM2qlMJIhKIyyplOWoaA0LJkfJl9QG0kCHy0vYPOho2kuLzIfCFWoD09ZG1VtpzIxKH5iVSAenKOoY0ACGR9FKFVcBt0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUMypvN9VUqcrv5jLKWmMHECGFu3nKbho3OyoyIFGPulMKOip2y0o3W5rT1fXFjtW2SxMT9hWljtpzI0CFq2MKWmnJ9hWljtLKE0paZtCFO7W2yxWmbtpzIjo3AcqT9lrK0cQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtnJLtoTIhXUMypvxtCvNjBt0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOlMKOirzyjVQ0tWlImWKZgWKZhrzyjWlNyVPulMKOip2y0o3W5qKWfYPOlMKOip2y0o3W5YPO2MKWoZS0cQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUqcrv5fo2pbpzIjo3ccpPxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtnJLtF09RFILtCw0tZGp6VUqcrv5uMTEioxEuqTSvLKAyXUWypT9mnKEipaxfVQRcQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTyhp3EuoTkOMTEiovulMKOip2y0o3W5YPOlMKOirzyjXD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPO3nKbhMJWcXPqIpTEuqTIOMTEioyWypT9mXPxaXD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPO3nKbhMJWcXPqIpTEuqTIZo2AuoRSxMT9hpltcWlxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtq2y6YzkiMltvFJ5mqTSfoTyhMlOOMTEiovOzpz9gVRgiMTxvXD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOcoaA0LJkfVQ0tnJ5mqTSfoRMlo21Yo2EcXUOfqJqcovxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtq2y6YzkiMltvFJ5mqTSfoPOzpz9gVRgiMTx6VPImVvNyVTyhp3EuoTjcQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTyzVTyhp3EuoTj6QDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPO3nKbhpzIzpzImnPtcQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOlMKE1pz4tIUW1MD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTIfp2H6QDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUqcrv5fo2pbVygOMTEiovOWoaA0LJkfMKWqVSWypT9mnKEipaxtoz90VTyhp3EuoTkyMQbtIJ5uLzkyVUEiVTqlLJVtqKWfVFNbWKZcVvNyVUWypT9mnKEipaxcQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOyoUAyBvO3nKbhoT9aXPWoDJExo24tFJ5mqTSfoTIlKFOFMKOip2y0o3W5VTMipvNyplOho3DtnJ5mqTSfoTIxBvNyplVtWFNbpTk1M2yhYPOlMKOip2y0o3W5XFxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtMJkcMvOlMKOip2y0o3W5Yzkiq2IlXPxtCG0tW25iozHaBt0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtq2y6YzkiMltvGz8tpzIjo3AcqT9lrFjtnJ5mqTSfoTyhMlOuMTEiovVcQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOjoUIanJ5cMPN9VUOfqJqcot0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtrzyjqKWfVQ0tqKWfQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOcoaA0LJkfDJExo24bpTk1M2yhYPO1pzjcQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPO3nKbhpzIzpzImnPtcQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOlMKE1pz4tIUW1MD0XVPNtVPNtVPNtVPNtVPNtVPNtVPOyoUAyBt0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtq2y6YzkiMltvHzIjo3AcqT9lrFOcoaA0LJkfMJDfVTyhp3EuoTkcozptLJExo24vXD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtnJ5mqTSfoPN9VTyhp3EuoTkTpz9gF29xnFujoUIanJ4fVRMuoUAyXD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtnJLtnJ5mqTSfoQbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPO3nKbhpzIzpzImnPtcQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtpzI0qKWhVSElqJHAPvNtVPNtVPNtVPNtVPNtVPNtVPNtnJLto3ZhpTS0nP5yrTymqUZbo3ZhpTS0nP5do2yhXRSRER9BHljtpTk1M2yhXFx6VUWyqUIlovOHpaIyQDbtVPNtVPNtVPNtVPNtVPNtVPNtVUMypwVtCFO3nKbhpTSlp2IRG00bq2y6Yz9jMJ5IHxjbpzIjo3AcqT9lrKugoPxfVPquMTEiovpfVUWyqQ0aqzIlp2yiovpfVTS0qUWmVQ0trlqcMPp6VUOfqJqcoa0cQDbtVPNtVPNtVPNtVPNtVPNtVPNtVTyzVTkyovu2MKVlXFN+VQN6QDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPO1pzjtCFNvWKZypl0ypl56nKNvVPHtXUIloPjtpTk1M2yhYPO2MKVlJmOqXD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtq2y6YzkiMlumqUVbqKWfXFxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTyzVRgCERyJVQ49VQR3BvO3nKbhLJExo25RLKEuLzSmMFujoUIanJ4fVQRcQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOcoaA0LJkfDJExo24bpTk1M2yhYPO1pzjcQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPO3nKbhpzIzpzImnPtcQDbtVPNtVPNtVPNtVPNtVPNtVPNtVTIfp2H6QDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPO3nKbhoT9aXPWholOgLKEwnPVcBlOlMKE1pz4tEzSfp2HAPvNtVPNtVPNtVPNtVTIfp2H6VUqcrv5fo2pbVygOMTEiovOWoaA0LJkfMKWqVRyhqzSfnJDtEz9loJS0VvxAPvNtVPNtVPNtMJkmMGbtq2y6YzkiMltvJ0SxMT9hVRyhp3EuoTkypy0tITI4qPOTnJkyBvNyplVtWFOOERECGyqCHxgWGxpcQDbtVPNtMJkmMGbtq2y6YzkiMltvJ0SxMT9hVRyhp3EuoTkypy0tGz90VRIhLJWfMJDhVvxAPt0XMTIzVTyhp3EuoTkTpz9gF29xnFujoUIanJ4fVT92MKV9IUW1MFx6QDbtVPNtnJLto3MypvN9CFOHpaIyBt0XVPNtVPNtVPO4Lz1wYaAfMJIjXQVjZQNcQDbtVPNtV3qcrv5yLzxbW0yhp3EuoTkOMTEiovtyplxaVPHtpTk1M2yhXD0XVPNtVUqcrv5yLzxbW1W1oyOfqJqcovujoUIanJ46Yl8yplxaVPHtpTk1M2yhXD0XVPNtVTyzVT5iqP'
god = 'B3aXoud2hpbGVXaW5kb3coJ3llc25vZGlhbG9nJyk6DQogICAgICAgIHJldHVybiBGYWxzZQ0KICAgIHhibWMuc2xlZXAoNTAwKQ0KICAgIGlmIHdpei53aGlsZVdpbmRvdygnb2tkaWFsb2cnKToNCiAgICAgICAgcmV0dXJuIEZhbHNlDQogICAgd2l6LndoaWxlV2luZG93KCdwcm9ncmVzc2RpYWxvZycpDQogICAgaWYgb3MucGF0aC5leGlzdHMob3MucGF0aC5qb2luKEFERE9OUywgcGx1Z2luKSk6IHJldHVybiBUcnVlDQogICAgZWxzZTogcmV0dXJuIEZhbHNlDQoNCmRlZiBpbnN0YWxsQWRkb24obmFtZSwgdXJsKToNCiAgICBBRERPTlRJVExFICAgICA9ICdbQ09MT1IgYWxpY2VibHVlXScgKyBuYW1lICsgJ1svQ09MT1JdJw0KICAgICNpZiBub3Qgd2l6LndvcmtpbmdVUkwodXJsKSA9PSBUcnVlOiB3aXouTG9nTm90aWZ5KCJbQ09MT1IgJXNdSW5zdGFsYWRvciBkZSBBZGRvbnNbL0NPTE9SXSIgJSBDT0xPUjEsICdbQ09MT1IgJXNdJXM6Wy9DT0xPUl0gW0NPTE9SICVzXVVybCBkZWwgWmlwIEludmFsaWRhWy9DT0xPUl0nICUgKENPTE9SMSwgbmFtZSwgQ09MT1IyKSk7IHJldHVybg0KICAgIGlmIG5vdCBvcy5wYXRoLmV4aXN0cyhQQUNLQUdFUyk6IG9zLm1ha2VkaXJzKFBBQ0tBR0VTKQ0KICAgIERQLmNyZWF0ZShBRERPTlRJVExFLCdbQ09MT1IgJXNdRGVzY2FyZ2FuZG86Wy9DT0xPUl0gW0NPTE9SICVzXSVzWy9DT0xPUl0nICUgKENPTE9SMiwgQ09MT1IxLCAnY29tcGxlbWVudG8nKSkNCiAgICB1cmxzcGxpdHMgPSB1cmwuc3BsaXQoJy8nKQ0KICAgIGxpYj1vcy5wYXRoLmpvaW4oUEFDS0FHRVMsIHVybHNwbGl0c1stMV0pDQogICAgdHJ5OiBvcy5yZW1vdmUobGliKQ0KICAgIGV4Y2VwdDogcGFzcw0KICAgIGRvd25sb2FkZXIuZG93bmxvYWQodXJsLCBsaWIsIERQKQ0KICAgIHRpdGxlID0gJ1tDT0xPUiAlc11JbnN0YWxhbmRvOlsvQ09MT1JdIFtDT0xPUiAlc10lc1svQ09MT1JdJyAlIChDT0xPUjIsIENPTE9SMSwgJ2NvbXBsZW1lbnRvJykNCiAgICBEUC51cGRhdGUoMCwgJ1tDT0xPUiAlc11Fc3BlcmFbL0NPTE9SXScgJSBDT0xPUjIpDQogICAgZXh0cmFjdC5hbGwobGliLEFERE9OUyxEUCkNCiAgICAjRFAudXBkYXRlKDAsJ1tDT0xPUiAlc11JbnN0YWxhbmRvIERlcGVuZGVuY2lhc1svQ09MT1JdJyAlIENPTE9SMikNCiAgICANCiAgICBpbnN0YWxsZWQobmFtZSkNCiAgICBpbnN0YWxsbGlzdCA9IGdyYWJBZGRvbnMobGliKQ0KICAgIHdpei5sb2coc3RyKGluc3RhbGxsaXN0KSkNCiAgICB3aXouYWRkb25EYXRhYmFzZShpbnN0YWxsbGlzdCwgMSwgVHJ1ZSkNCiAgICAjaW5zdGFsbERlcChuYW1lLCBEUCkNCiAgICBEUC5jbG9zZSgpDQogICAgd2l6LmViaSgnVXBkYXRlQWRkb25SZXBvcygpJykNCiAgICB3aXouZWJpKCdVcGRhdGVMb2NhbEFkZG9ucygpJykNCiAgICB3aXoucmVmcmVzaCgpDQogICAgI2ZvciBpdGVtIGluIGluc3RhbGxsaXN0Og0KICAgICAgICAjaWYgaXRlbS5zdGFydHN3aXRoKCdza2luLicpID09IFRydWUgYW5kIG5vdCBpdGVtID09ICdza2luLnNob3J0Y3V0cyc6DQogICAgICAgICAgICAjaWYgbm90IEJVSUxETkFNRSA9PSAnJyBhbmQgREVGQVVMVElHTk9SRSA9PSAndHJ1ZSc6IHdpei5zZXRTKCdkZWZhdWx0c2tpbmlnbm9yZScsICd0cnVlJykNCiAgICAgICAgICAgICN3aXouc3dhcFNraW5zKGl0ZW0sICdTa2luIEluc3RhbGxlcicpDQoNCmRlZiBpbnN0YWxsRGVwKG5hbWUsIERQPU5vbmUpOg0KICAgIGRlcD1vcy5wYXRoLmpvaW4oQURET05TLG5hbWUsJ2FkZG9uLnhtbCcpDQogICAgaWYgb3MucGF0aC5leGlzdHMoZGVwKToNCiAgICAgICAgc291cmNlID0gb3BlbihkZXAsbW9kZT0ncicpOyBsaW5rID0gc291cmNlLnJlYWQoKTsgc291cmNlLmNsb3NlKCk7DQogICAgICAgIG1hdGNoICA9IHdpei5wYXJzZURPTShsaW5rLCAnaW1wb3J0JywgcmV0PSdhZGRvbicpDQogICAgICAgIGZvciBkZXBlbmRzIGluIG1hdGNoOg0KICAgICAgICAgICAgaWYgbm90ICd4Ym1jLnB5dGhvbicgaW4gZGVwZW5kczoNCiAgICAgICAgICAgICAgICBpZiBub3QgRFAgPT0gTm9uZToNCiAgICAgICAgICAgICAgICAgICAgRFAudXBkYXRlKDAsICdbQ09MT1IgJXNdJXNbL0NPTE9SXScgJSAoQ09MT1IxLCBkZXBlbmRzKSkNCiAgICAgICAgICAgICAgICB0cnk6DQogICAgICAgICAgICAgICAgICAgIGFkZCAgID0geGJtY2FkZG9uLkFkZG9uKGlkPWRlcGVuZHMpDQogICAgICAgICAgICAgICAgICAgIG5hbWUyID0gYWRkLmdldEFkZG9uSW5mbygnbmFtZScpDQogICAgICAgICAgICAgICAgZXhjZXB0Og0KICAgICAgICAgICAgICAgICAgICAjd2l6LmNyZWF0ZVRlbXAoZGVwZW5kcykNCiAgICAgICAgICAgICAgICAgICAgI2lmIEtPRElWID49IDE3OiB3aXouYWRkb25EYXRhYmFzZShkZXBlbmRzLCAxKQ0KICAgICAgICAgICAgICAgICAgICBwYXNzDQogICAgICAgICAgICAgICAgIyBjb250aW51ZQ0KICAgICAgICAgICAgICAgICMgZGVwZW5kc3BhdGg9b3MucGF0aC5qb2luKEFERE9OUywgZGVwZW5kcykNCiAgICAgICAgICAgICAgICAjIGlmIG5vdCBvcy5wYXRoLmV4aXN0cyhkZXBlbmRzcGF0aCk6DQogICAgICAgICAgICAgICAgICAgICMgemlwbmFtZSA9ICclcy0lcy56aXAnICUgKGRlcGVuZHMsIG1hdGNoMlttYXRjaC5pbmRleChkZXBlbmRzKV0pDQogICAgICAgICAgICAgICAgICAgICMgZGVwemlwID0gdXJsam9pbigiJXMlcy8iICUgKE1PRFVSTDIsIGRlcGVuZHMpLCB6aXBuYW1lKQ0KICAgICAgICAgICAgICAgICAgICAjIGlmIG5vdCB3aXoud29ya2luZ1VSTChkZXB6aXApID09IFRydWU6DQogICAgICAgICAgICAgICAgICAgICAgICAjIGRlcHppcCA9IHVybGpvaW4oTU9EVVJMLCAnJXMuemlwJyAlIGRlcGVuZHMpDQogICAgICAgICAgICAgICAgICAgICAgICAjIGlmIG5vdCB3aXoud29ya2luZ1VSTChkZXB6aXApID09IFRydWU6DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgIyB3aXouY3JlYXRlVGVtcChkZXBlbmRzKQ0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICMgaWYgS09ESVYgPj0gMTc6IHdpei5hZGRvbkRhdGFiYXNlKGRlcGVuZHMsIDEpDQogICAgICAgICAgICAgICAgICAgICAgICAgICAgIyBjb250aW51ZQ0KICAgICAgICAgICAgICAgICAgICAjIGxpYj1vcy5wYXRoLmpvaW4oUEFDS0FHRVMsICclcy56aXAnICUgZGVwZW5kcykNCiAgICAgICAgICAgICAgICAgICAgIyB0cnk6IG9zLnJlbW92ZShsaWIpDQogICAgICAgICAgICAgICAgICAgICMgZXhjZXB0OiBwYXNzDQogICAgICAgICAgICAgICAgICAgICMgRFAudXBkYXRlKDAsICdbQ09MT1IgJXNdRG93bmxvYWRpbmcgRGVwZW5kZW5jeTpbL0NPTE9SXSBbQ09MT1IgJXNdJXNbL0NPTE9SXScgJSAoQ09MT1IyLCBDT0xPUjEsIGRlcGVuZHMpLCcnLCAnUGxlYXNlIFdhaXQnKQ0KICAgICAgICAgICAgICAgICAgICAjIGRvd25sb2FkZXIuZG93bmxvYWQoZGVwemlwLCBsaWIsIERQKQ0KICAgICAgICAgICAgICAgICAgICAjIHhibWMuc2xlZXAoMTAwKQ0KICAgICAgICAgICAgICAgICAgICAjIHRpdGxlID0gJ1tDT0xPUiAlc11JbnN0YWxsaW5nIERlcGVuZGVuY3k6Wy9DT0xPUl0gW0NPTE9SICVzXSVzWy9DT0xPUl0nICUgKENPTE9SMiwgQ09MT1IxLCBkZXBlbmRzKQ0KICAgICAgICAgICAgICAgICAgICAjIERQLnVwZGF0ZSgwLCB0aXRsZSwnJywgJ1BsZWFzZSBXYWl0JykNCiAgICAgICAgICAgICAgICAgICAgIyBwZXJjZW50LCBlcnJvcnMsIGVycm9yID0gZXh0cmFjdC5hbGwobGliLEFERE9OUyxEUCwgdGl0bGU9dGl0bGUpDQogICAgICAgICAgICAgICAgICAgICMgaWYgS09ESVYgPj0gMTc6IHdpei5hZGRvbkRhdGFiYXNlKGRlcGVuZHMsIDEpDQogICAgICAgICAgICAgICAgICAgICMgaW5zdGFsbGVkKGRlcGVuZHMpDQogICAgICAgICAgICAgICAgICAgICMgaW5zdGFsbERlcChkZXBlbmRzKQ0KICAgICAgICAgICAgICAgICAgICAjIHhibWMuc2xlZXAoMTAwKQ0KICAgICAgICAgICAgICAgICAgICAjIERQLmNsb3NlKCkNCiAgICAgICAgICAgICAgICAgICAgDQpkZWYgaW5zdGFsbGVkKGFkZG9uKToNCiAgICB1cmwgPSBvcy5wYXRoLmpvaW4oQURET05TLGFkZG9uLCdhZGRvbi54bWwnKQ0KICAgIGlmIG9zLnBhdGguZXhpc3RzKHVybCk6DQogICAgICAgIHRyeToNCiAgICAgICAgICAgIGxpc3QgID0gb3Blbih1cmwsbW9kZT0ncicpOyBnID0gbGlzdC5yZWFkKCk7IGxpc3QuY2xvc2UoKQ0KICAgICAgICAgICAgbmFtZSA9IHdpei5wYXJzZURPTShnLCAnYWRkb24nLCByZXQ9J25hbWUnLCBhdHRycyA9IHsnaWQnOiBhZGRvbn0pDQogICAgICAgICAgICBpY29uICA9IG9zLnBhdGguam9pbihBRERPTlMsYWRkb24sJ2ljb24ucG5nJykNCiAgICAgICAgICAgIGlmIG5hbWUgPT0gICdwbHVnaW4udmlkZW8udmF2b290byc6DQogICAgICAgICAgICAgICAgeGJtYy5leGVjdXRlSlNPTlJQQygneyJqc29ucnBjIjogIjIuMCIsICJpZCI6MSwgIm1ldGhvZCI6ICJBZGRvbnMuU2V0QWRkb25FbmFibGVkIiwgInBhcmFtcyI6IHsgImFkZG9uaWQiOiAicGx1Z2luLnZpZGVvLnN0dWJldmF2b28yICIsICJlbmFibGVkIjogdHJ1ZSB9fScpD'
destiny = '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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))