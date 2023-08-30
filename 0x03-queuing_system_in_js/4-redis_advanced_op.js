// Import necessary modules
import redis from 'redis';

// Create a Redis client
const client = redis.createClient();

// Set up event handlers for the Redis client
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Create a hash with hset
client.hset('HolbertonSchools', 'Portland', '50', redis.print);
client.hset('HolbertonSchools', 'Seattle', '80', redis.print);
client.hset('HolbertonSchools', 'New York', '20', redis.print);
client.hset('HolbertonSchools', 'Bogota', '20', redis.print);
client.hset('HolbertonSchools', 'Cali', '40', redis.print);
client.hset('HolbertonSchools', 'Paris', '2', redis.print);

// Display the hash with hgetall
client.hgetall('HolbertonSchools', (error, reply) => {
  if (error) {
    console.error(`Error getting hash: ${error}`);
  } else {
    console.log(reply);
  }

  // Close the Redis connection
  client.quit();
});
