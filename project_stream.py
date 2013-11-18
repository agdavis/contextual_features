from Tweetstream import *

if __name__ == "__main__":
     print "Criando o stream"
     ts = Tweetstream(sys.argv[1])
     print "Criado o stream"
     ts.project_stream_features(["id", "user", "created_at", "text"], sys.argv[2])
